# investing_competition
by Junmai [github](https://github.com/jonas-jun/investing_competition), 2020-08-01
***
Program to Manage Investing Competition
---

### 결과물

    1. 전날 집계 파일을 read 하고
    2. 대회 참가 종목 종가를 매일 크롤링
    3. 기준가(대회 시작일 가격)를 기준으로 수익률을 산정한 후
    4. 수익률 기준 랭킹 sorting 하여
    5. 엑셀파일로 write

### 구현요소

    1. 전날 날짜의 엑셀 파일 (gjy_2020-07-22.xlsx)를 read (import sheet)
    2. 홀딩하지 않은 종목(비고 column이 비어있는)들의 code list를 생성
    3. code list 종목들의 당일 종가를 크롤링하여 새로운 column에 넣기
    4. 홀딩 종목들은 전날 가격을 당일 column에 그대로 넣기
    5. 당일 column과 기준가를 기준으로 새로운 수익률 산정
    6. 수익률 기준으로 내림차순 sorting하고 순위와 변동 계산
    7. gjy_오늘 날짜.xlsx (gjy_2020-07-23.xlsx)의 형태로 write (export sheet)

### 체크포인트

    1. import sheet 전에 전날에 새로 홀딩한 내용을 '비고' column에 표기
    2. 월요일의 경우, 지난 금요일 파일명을 일요일 파일명으로 바꿔두면 편함 (또는 import sheet 함수에 date= argument를 금요일로 바꿔줄 수도 있음)
    3. 엑셀에서 read 했을 때 2020-07-23 이 2020-07-23 00:00:00 format으로 바뀌어 있음. 따라서 어제의 column을 다시 2020-07-23 형태로 바꿔주는 작업을 거쳐야 함 (함수에 추가?)
