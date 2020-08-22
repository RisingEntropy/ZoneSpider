import DataAnalyze


class LogInfo:
    cookie = {}
    usr = '1724458359'
    host = '326886560'


def getg_tk(p_skey):
    has = int(5381)
    for i in p_skey:
        has += (has << 5) + ord(i)
        hash = has & 2147483647
    return hash


info = LogInfo
sheet = DataAnalyze.Sheet()
tempTable = {}  # 这个字典用于储存QQ号->Visitor对象的映射
