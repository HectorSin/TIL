# 인수인계 파일 분석

Pred_server - 예측 서버 폴더



Sensor_server - RP로부터 센서 데이터를 전송받고 저장하는 폴더



Smartfarm은 스마트팜 제안서 관련 코딩을 위해 테스트했던 폴더



Parsing_sensor.py는 라즈베리파이에 있는 파일을 그대로 가져와 백업한 것



**Pred_server와 Sensor_server는 systemctl을 이용해 부팅 시 자동으로 작동되도록 구성**

### systemctl

- systemctl은 리눅스 시스템에서 시스템 서비스와 데몬을 관리하는 유틸리티입니다. 이 명령을 사용하여 시스템 부팅 시 자동으로 시작되는 서비스나 데몬을 관리하고, 서비스의 상태를 확인하며, 시작/정지/재시작 및 기타 작업을 수행할 수 있습니다. systemctl은 대부분의 현대적인 리눅스 배포판에서 사용되며, 시스템 관리자가 시스템 구성을 관리하고 모니터링하는 데 도움이 됩니다.



# Pred_server

발전량 예측 시제품 폴더. Pred_server.py가 해당 서버임

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
    data['energy'] = data['ws'] * 20
    values = data.values[-2160:].reshape(5, 2160).astype(np.float32)
    
    mins = np.min(values, axis=1).reshape(5,1)
    maxs = np.max(values, axis=1).reshape(5,1)
    values = (values - mins) / (maxs - mins) # 모델 입력을 위해 scaling
    output = predict(values[None, :, :]) # 모델 출력값 획득
    prediction = output * (maxs - mins) + mins # 모델 출력값 rescaling
    prediction = prediction[-1, :]
```

