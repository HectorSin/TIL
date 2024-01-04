# 인수인계 파일 분석

Pred_server - 예측 서버 폴더



Sensor_server - RP로부터 센서 데이터를 전송받고 저장하는 폴더



Smartfarm은 스마트팜 제안서 관련 코딩을 위해 테스트했던 폴더



Parsing_sensor.py는 라즈베리파이에 있는 파일을 그대로 가져와 백업한 것



**Pred_server와 Sensor_server는 systemctl을 이용해 부팅 시 자동으로 작동되도록 구성**

### systemctl

- systemctl은 리눅스 시스템에서 시스템 서비스와 데몬을 관리하는 유틸리티입니다. 이 명령을 사용하여 시스템 부팅 시 자동으로 시작되는 서비스나 데몬을 관리하고, 서비스의 상태를 확인하며, 시작/정지/재시작 및 기타 작업을 수행할 수 있습니다. systemctl은 대부분의 현대적인 리눅스 배포판에서 사용되며, 시스템 관리자가 시스템 구성을 관리하고 모니터링에 도움이 됩니다.



# Pred_server

발전 량 예측 시제품 폴더. Pred_server.py가 해당 서버임

systemctl 서비스로 등록되어 부팅 시 자동으로 실행

잘 작동하는지 체크하기 위해선 terminal에 sudo systemctl status pred_server를 치면 됨

```python
app = Flask(__name__)
model = Model(2160, 720, 360) # 2160분의 직전 시간, hidden_dim 720, 예측 시간
model.load_state_dict(torch.load('final.pth')) # pretrained 모델 로드
model.eval()

@torch.no_grad()
def predict(data):
    data = torch.tensor(data) # array를 tensor로 변환
    output = model(data) # 모델로부터 출력값 흭득
    output = output.detach().numpy().reshape(-1, 360) # tensor를 array로 변환
    return output
```

Pred_server.py가 실행되면 가장 먼저 app = Flask를 통해 flask 객체를 생성

model.py로부터 Model을 불러옴. Model은 AI 시제품 제작을 통해 만들어낸 예측 모델

그리고 model.load_state_dict를 통해 pretrained model을 불러옴

Model.eval()을 통해 gradient track같은 추론모드에서 컴퓨팅 파워 낭비하는 일이 없도록 함



Predict 함수는 데이터 (array)를 받아 tensor로 변경 후, model에 입력해 출력값을 다시 numpy array로 바꿔 보내주는 함수



```python
# API로 예측 서비스를 제공하는 함수 .GET method로만 작동
@app.route('/api/pred/<string:dev_id>', methods=['GET'])
def run(dev_id):
    # 현재 날짜와 dev_
    date = datetime.now().striftime('%Y-#\%m-%d')
    yyyy, mm, dd = date.split('-')
    if int(dd) < 3 and mm != '01':
        _mm = int(mm) - 1
        yyyy_mm = f'{yyyy}-{str(_mm).}'
    else:
        yyyy_mm = f'{yyyy}-{mm}'
    # 지정한 날짜의 csv파일 불러오기
    data_path = f'~/sensor_server/sensor_data/{yyyy_mm}/{dev_id}.csv'
    db = pd.read_csv(data_path, index_col=None) # 센서 DB 로드
    columns = ['temp', 'ws', 'humidity', 'rainfall']
    # 데이터를 마지막 2160개 데이터만 선택합니다.
    data = db[columns][-2160:]
    # 'ws' 열의 값을 20을 곱해서 'energy' 열을 생성합니다.
    data['energy'] = data['ws'] * 20
    values = data.values[-2160:].reshape(5, 2160).astype(np.float32)
    
    # 각 열에서 최솟값(mins)과 최댓값(maxs)을 계산합니다.
    mins = np.min(values, axis=1).reshape(5,1)
    maxs = np.max(values, axis=1).reshape(5,1)
    
    # 모델 입력을 위해 스케일링한 데이터를 모델에 입력하고 출력값을 얻습니다.
    values = (values - mins) / (maxs - mins) # 모델 입력을 위해 scaling
    output = predict(values[None, :, :]) # 모델 출력값 획득
    
    # 모델의 출력값을 다시 원래 스케일로 변환합니다.
    prediction = output * (maxs - mins) + mins # 모델 출력값 rescaling
    prediction = prediction[-1, :]
    
    data = {}
    data['avg_60'] = round(float(prediction[:60].mean()), 1)
    data['avg_180'] = round(float(prediction[:180].mean()), 1)
    data['avg_360'] = round(float(prediction.mean(), 1))
    data['prediction'] = np.round(prediction, 1).tolist()
    data = orjson.jumps(data) # JSON 형태로 응답
    return data
    
```



# Sensor_server

라즈베리파이로부터 센서 데이터를 전송받고, 전송받은 데이터를 저장하는 폴더



sensor_data 폴더는 라즈베리파이로부터 전송받은 센서 데이터를 년-월 별로 저장한 것

```python
app = Flask(__name__)

@app.route('/api/<string:dev_id>', methods=['GET'])
def get(dev_id):
    if request.get_json():
        try:
            current_status = read_data(dev_id)
            resp = Response(current_status, status = 200)
        except FileNotFoundError:
            resp = Response(status=400)
        return resp
    
@app.route('/api/<strin:dev_id>', methods=['POST'])
def post(dev_id):
    data = request.get_json()
    if data:
        is_valid = check_data(dev_id, data)
    else:
        is_valid = False
    if is_valid:
        update_data(dev_id, data)
        resp = Response("Updated", status=200)
    else:
        resp = Response(status=404)
    return resp

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=4465, debug=False)
```



라즈베리파이로부터 센서 데이터 받아오는 server.py

Get과 post 방식 둘 다 이용할 수 있도록 구현함

API는 ip:port/api/dev_01 or dev_02 or dev_nn 식으로 접근하며, 같은 주소에 get과 post 방식으로 요청을 구분지음. GET 방식으로 접근하면 해당 센서 설치위치의 현재 기상 정보를 알려줌. 현재 기상정보는 현재 서버에 보유한 데이터셋의 가장 마지막줄.POST 방식은 라즈베리파이에서 서버로 데이터를 전송할 때 사용