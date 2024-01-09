from flask import Flask, request, jsonify
import os
import pandas as pd
from datetime import datetime

app = Flask(__name__)

# 경로 설정: 현재 날짜에 해당하는 폴더와 파일 경로
current_date = datetime.now().strftime("%Y-%m")
data_folder = os.path.join("sensor_data", current_date)
csv_file_path = os.path.join(data_folder, "dev_02.csv")

@app.route('/get_data', methods=['GET'])
def get_data():
    try:
        # CSV 파일을 읽어와서 데이터프레임으로 변환
        df = pd.read_csv(csv_file_path)
        
        # 가장 마지막 행의 데이터 추출
        last_row = df.iloc[-1].to_dict()
        
        return jsonify(last_row), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/post_data', methods=['POST'])
def post_data():
    try:
        # POST 요청 데이터를 JSON으로 파싱
        data = request.json

        # 데이터 처리 및 저장 로직 추가
        # 여기에 데이터를 저장하거나 처리하는 코드를 추가하세요.

        return jsonify({"message": "Data received and processed successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
