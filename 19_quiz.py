# Quiz) 부동산 매물(송사 헬리오시티) 정보를 스크래핑 하는 프로그램을 만드시오

# [조회 조건]
# 1. http://daum.net 접속
# 2. '송파 헬리오시티' 검색
# 3. 다음 부동산 부분에 나오는 결과 정보
# [주의 사항]
# 실습하는 시점에 위 매물이 없다면 다른 곳으로 대체 가능
# [출력 결과]
# =========== 매물 1 ===========
# 거래 : 매매
# 면적 : 84/59(공급/전용)
# 가격 : 165,000 (만원)
# 동 : 214 동
# 층 : 고/23
# =========== 매물 2 ===========
# ....

import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}
url = "https://search.daum.net/search?w=tot&DA=UME&t__nil_searchbox=suggest&sug=&sugo=15&sq=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4&o=1&q=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0"
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

houses = soup.find("table", attrs={"class": "tbl"}).find(
    "tbody").find_all("tr")
for idx, house in enumerate(houses):
    columns = house.find_all("td")
    if len(columns) <= 1:  # 의미 없는 데이터를 skip
        continue
    data = [column.get_text() for column in columns]
    print(f"=========== 매물 {idx+1}==============")
    print(f"거래 : {data[0].strip()}")
    print(f"면적 : {data[1].strip()}", "(공급/전용)")
    print(f"가격 : {data[2].strip()}", "(만원)")
    print(f"동 : {data[3].strip()}")
    print(f"층 : {data[4].strip()}")
