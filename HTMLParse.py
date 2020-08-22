from lxml import etree
import DataAnalyze
import Loginfo



def countLike(htmlcode):
    html = etree.HTML(htmlcode)
    userlist = html.xpath('//div[@class="user-list"]/a/@href')
    for i in userlist:
        if i[25:] in Loginfo.tempTable:
            Loginfo.tempTable[i[25:]].like += 1
        else:
            Loginfo.tempTable.update({i[25:]: DataAnalyze.Visitor(i[25:])})  # 不存在此人则创建
            Loginfo.tempTable[i[25:]].like += 1


def countComment(htmlcode):
    html = etree.HTML(htmlcode)
    userlist = html.xpath('//div[@class="comments-content"]/a/@href')
    for i in userlist:
        if i[25:] in Loginfo.tempTable:
            Loginfo.tempTable[i[25:]].comment += 1
        else:
            Loginfo.tempTable.update({i[25:]: DataAnalyze.Visitor(i[25:])})
            Loginfo.tempTable[i[25:]].comment += 1
