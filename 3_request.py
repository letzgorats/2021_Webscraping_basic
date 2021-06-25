import requests
res = requests.get("http://google.com")
#res = requests.get("http://nadocodings.tistory.com")
print("응답코드 : ", res.status_code)  # 200 이면 정상
res.raise_for_status()
# res.raiste_for_status()를 만나면
# 문제가 있다면 바로 종료를 하고
# 문제가 없다면 다음 코드를 진행한다.
# re = requests.get("사이트")와 res.raise_for_status()는
# 쌍으로 쓰는게 국룰이다.
print("웹 스크랩핑을 진행합니다")

# if res.status_code == requests.codes.ok:
#     print("정상입니다")
# else:
#     print("문제가 생겼습니다. [에러코드 ", res.status_code, "]")

print(len(res.text))
# print(res.text)
with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)
