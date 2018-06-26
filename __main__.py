import sys
import collect
from visualize import visualizer
from analize import analyzer
from config import CONFIG

#
# sys.path.append('/pychamProjects/python-modules')
# ## analysus_fb를 실행시켜줌
# from analysis_fb.collect import  crawler as cw



if __name__ == '__main__':


    # for item in items
    items = [{'pagename':'jtbcnews','since':'2017-01-01','until': '2017-12-31'},
                 {'pagename':'chosun','since':'2017-01-01','until': '2017-12-31'}]
    #
    #     # 데이터 수집
    for item in items:
        collect.crawling(**item)


   # 데이터 수집(collection)
# for item in items:
#     resultfile = collect.crawling(**item, fetch=False)
#     item['resultfile'] = resultfile
#
# # 데이터 분석(analyze)
# for item in items:
#     data = analyzer.json_to_str(item['resultfile'], 'message')
#     item['count_wordfreq'] = analyzer.count_wordfreq(data)
#
# # 데이터 시각화(visualize)
# for item in items:
#     count = item['count_wordfreq']
#     count_m50 = dict(count.most_common(50))
#
#     filename = "%s_%s_%s" % (item['pagename'], item['since'], item['until'])
#     visualizer.wordcloud(filename, count_m50)
#
#     visualizer.graph_bar(
#                         title = '%s 빈도 분석' % (item['pagename']),
#                         xlabel = '단어',
#                         ylabel = '빈도수',
#                         values = list(count_m50.values()), # values y출 값
#                         ticks = list(count_m50.keys()), # key 값 = 기사 내용
#                         showgrid = False,
#                         filename = filename,
#                         showgraph = False # 팝업윈도우를 안뜨고, 바로 파일로 저장하겠다.
#                         )


    #데이터 수집

    # 데이터 분석
    # for item in items:
    #     print(item['resultfile'])
