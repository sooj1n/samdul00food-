from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import csv
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    #allow_origins=["http://localhost:8023"],  # 허용할 출처 (클라이언트 URL
    allow_origins=["https://samdul23food.web.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
	return {"Hello": "n23"}

@app.get("/food")
def food(name:str):
    # 시간 구하기
    now = datetime.now()
    t = now.strftime('%Y-%m-%d %H:%M:%S')
    print("=================================" + name)
    print("=================================" + t)

    # 저장 경로
    #home_dir = os.path.expanduser('~')
    directory = 'data'
    print("**********************************" + directory)

    # 폴더가 없는 경우 폴더 생성
    if not os.path.exists(directory):
        os.makedirs(directory)

    # CSV 파일 경로
    csv_file_path = f'{directory}/food.csv'

    # 데이터 저장
    data = {"Name": name, "time": t}

    # CSV 파일이 비어 있는지 확인 후 헤더 작성
    file_exists = os.path.exists(csv_file_path) and os.stat(csv_file_path).st_size > 0

    # CSV 파일에 데이터 쓰기
    with open(csv_file_path, mode='a', newline='') as file:  # append 모드로 열기
        fieldnames = ['Name', 'time']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # 파일이 존재하지 않거나 비어 있을 때 헤더 작성
        if not file_exists:
            writer.writeheader()

        # 단일 행 쓰기
        writer.writerow(data)

    return {"food": name, "time": t}



