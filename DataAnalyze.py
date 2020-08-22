import xlwt
import os
import Network
import threading
import demjson
import re
import HTMLParse


class Visitor:
    uin = '木有找到QQ号'
    sex = '未知'
    comment = 0
    like = 0
    isFriend = False
    nickname = '木有查询到'

    def __init__(self, uin, sex='未知'):
        self.uin = uin
        self.sex = sex

    def __lt__(self, other):
        return self.like > other.like

    def spideInfo(self):
        dic = Network.getUserInfo(self.uin)
        self.sex = dic['gender']
        self.nickname = dic['nickname']
        self.isFriend = bool(dic['isFriend'])


patt = re.compile(".*?({.*}).*")


def loads_jsonp(_jsonp):
    try:
        return demjson.decode(re.match(".*?({.*}).*", _jsonp, re.S).group(1))
    except:
        raise ValueError('Invalid Input')


threadpool = {}


class Analyze(threading.Thread):
    def __init__(self, lock, file, id, filename):
        threading.Thread.__init__(self)
        self.lock = lock
        self.file = file
        self.id = id
        self.filename = filename

    def run(self):
        text = self.file.read()
        res = loads_jsonp(text)
        if not str(res['code']) == '0':
            print("错误发生，返回代码：%s" % str(res['code']))
            return
        try:
            reda = res['data']['friend_data']
        except KeyError:
            print("解析缓存 %s 时出现错误，线程%d退出" % (self.filename, self.id))
            return
        leng = len(reda)

        for i in range(0, leng - 1):
            self.lock.acquire()
            HTMLParse.countLike(reda[i]['html'])
            HTMLParse.countComment(reda[i]['html'])
            self.lock.release()
        self.file.close()
        del threadpool[self.id]

Item = ['QQ号', 'Nickname', '点赞数', '评论数', '是否是好友', '性别']


class Sheet:
    def __init__(self):
        self.users = []

    def append(self, vis):
        self.users.append(vis)

    def writeToExcel(self):
        workbook = xlwt.Workbook()
        sheet = workbook.add_sheet("INFO")
        pos = 0
        for i in Item:
            sheet.write(0, pos, i)
            pos += 1
        col = 1
        self.users.sort()
        for i in self.users:
            try:
                i.spideInfo()
            except Exception as e:
                print("Error when getting gender,omitted")
            sheet.write(col, 0, i.uin)
            sheet.write(col, 1, i.nickname)
            sheet.write(col, 2, i.like)
            sheet.write(col, 3, i.comment)
            sheet.write(col, 4, "Yes" if i.isFriend else 'No')
            sheet.write(col, 5, i.sex)
            col += 1
        if not os.path.exists('result'):
            os.mkdir('result')
        workbook.save('result/Result.xls')