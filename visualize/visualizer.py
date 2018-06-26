import os
import pytagcloud
import matplotlib.pyplot as plt
import collections



RESULT_DIRECTORY = "__result__/visualization"


def wordcloud(filename,wordfreq):
    taglist = pytagcloud.make_tags(wordfreq.items(),maxsize=80)
    #print(taglist)
    save_filename = '%s/wordcloud_%s.jpg' % (RESULT_DIRECTORY,filename)
    pytagcloud.create_tag_image(taglist,
                                save_filename,
                                size = (900,600),
                                fontname= 'Malgun',
                                rectangular = False,
                                background = (0,0,0)
                                )
def graph_bar(
        # bar그래프 필수 파라미터
        title = None, xlabel = None, ylabel = None, showgrid = False,
        values = None,ticks = None, filename = None, showgraph = True):

    fig, subplots = plt.subplots(1, 1)
    subplots.bar(range(len(values)), values, align = 'center')

    # ticks -> x축
    if ticks is not None and isinstance(ticks,collections.Sequence):
        subplots.set_xticks(range(len(ticks)))
        subplots.set_xticklabels(ticks, rotation=80, fontsize='xx-small')
    #title
    if title is not None and isinstance(title, str):
        subplots.set_title(title)

    #xlabel
    if title is not None and isinstance(title, str):
        subplots.set_xlabel(xlabel)
    #ylabel

    if title is not None and isinstance(title, str):
        subplots.set_ylabel(ylabel)

    # showgrid -- > 데코
    subplots.grid(showgrid)


    if filename is not None and isinstance(filename,str):
        save_filename = '%s/bar_%s.png' % (RESULT_DIRECTORY,filename)
        plt.savefig(save_filename, dpi = 400, bbox_inches = 'tight')
        # 해상도 400, 여백을 주지않음


    # show graph
    if showgraph:
        plt.show()


 # 디렉토리 여부 조사
if os.path.exists(RESULT_DIRECTORY) is False:
    os.mkdir(RESULT_DIRECTORY)