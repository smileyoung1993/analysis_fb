
# browser 만들기

# html 받기
from urllib.request import  Request,urlopen
from datetime import *
import sys

try:
    url= "http://www.naverddddd.com"

    Request(url)  # request객체 생성

    request = Request(url)
    resp = urlopen(request)

    # 응답내용을 다 읽는다.
    resp_body = resp.read().decode("utf-8")
    print(resp_body)

except Exception as e:
    print('%s %s' % (e,datetime.now()),file = sys.stderr) #standard err
