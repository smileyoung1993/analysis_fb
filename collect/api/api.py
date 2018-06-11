
# FB API WRAPPER FUNCTIONS
from urllib.parse import urlencode
from .json_request import json_request # 현디렉토리 .  /  상위 디렉토리 ..

ACCESS_TOKEN = "EAACEdEose0cBAFG7MV38i5Esffql9nlZAwhwioNEZAuAZAy1iMFOD6SkDJbQ46j9AyGsAEbhZC0E6NgXBF2fHZCZAiMgZCJVtPXfb5kSOxQcBRZAoc8007u8aqywZBxDnXDw5QHlZBV6T9ZB8RNAkYh9nFVKAFpaoZBCqIcyEyed7066ShWC2FxRqEoULCIYvwbN86wZD"

BASE_URL_FB_API = "https://graph.facebook.com/v3.0"



# **params => 딕션너리 상태로 저장
def fb_gen_url(base = BASE_URL_FB_API,node ='', **params):# **params 으로 들어온 값을 dict로 받는다.

    # base = 상수, 변하지 않는 파라미터

    url = '%s/%s/?%s' % (base,node,urlencode(params)) # urlencode는 쿼리스트링으로 만들어준다.

    return url


def fb_name_to_id(pagename):

    url = fb_gen_url(node = pagename, access_token = ACCESS_TOKEN)

    json_result = json_request(url = url)
    print(type(json_result))
    return json_result.get("id")

def fb_fetch_posts(pagename, since, until):

    url = fb_gen_url(node=fb_name_to_id(pagename) + "/posts",
                     fields='id,message,link,name,type,shares,reactions,created_time,comments.limit(0).summary(true).limit(0).summary(true)',
                     since=since, until=until, limit=50, access_token=ACCESS_TOKEN)

    #print(url)
    print("-------------------------------")
    json_result = json_request(url=url)
    print(json_result)
