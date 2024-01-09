import requests

# 서버 정보 및 개발자 ID 설정
SERVER, PORT = '54.180.106.155', 4465  # AWS
DEV_ID = 'dev_02'

url = f'http://{SERVER}:{PORT}/api/{DEV_ID}'
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
data_j = {'timestamp': 1704784137, 'ip': '58.72.215.20', 'temp': 25.2, 'humidity': 23.5, 'ws': 0.0, 'wd': 274, 'north_direction': 104.5, 'atmospheric_pressure': 1013.8, 'rainfall': 0.0, 'voltage': 12.2}
def receive_data():
    try:
        # GET 요청을 보내되, 빈 JSON 본문을 포함시킴
        response = requests.get(url, headers=headers, json=data_j, timeout=5)
        if response.status_code == 200:
            # 성공적으로 데이터를 받아왔을 때
            data = response.json()
            return data
        else:
            # 오류 발생시 상태 코드 출력
            print(f"Failed to retrieve data. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        # 요청 중 예외 발생시 출력
        print(f"Request error: {e}")
    return None

# 메인 함수
if __name__ == '__main__':
    data = receive_data()
    if data:
        # 받아온 데이터 처리 (예: 출력)
        print(data)
