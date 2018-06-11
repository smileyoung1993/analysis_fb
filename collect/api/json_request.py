from urllib.request import  Request,urlopen
from datetime import *
import sys
import json

def json_request(url='',
    encoding = 'utf-8',
    success = None,
    error = lambda e:print('%s %s' % (e,datetime.now()),file = sys.stderr)):

    try:
        Request(url)  # request객체 생성
        request = Request(url)
        resp = urlopen(request)


    # 응답내용을 다 읽는다.
        html = resp.read().decode(encoding)
        json_result = json.loads(html)

        #print('%s : success for request[%s]' % (datetime.now(), url))

        if callable(success) is False:
            # success = None이 여서 html이 return됨 , 함수인지 아닌지를 판별
            return json_result
            # return값을 주는 의미는 바깥에서 처리해라 뜻

          #else
        success(json_result)

    except Exception as e:
         if callable(error) is True:
             error(e)


# html_request(url='http://www.naver.com', success=print, error=print)
#json_request(url='http://kickscar.cafe24.com:8080/myapp-api/api/user/list', success=print, error=print)