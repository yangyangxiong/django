import time
import datetime

now_time = datetime.datetime.now()
yes_time = now_time + datetime.timedelta(days=-1)
yesterday = yes_time.strftime('%Y%m%d')
today = now_time.strftime('%Y%m%d')

month_time = yes_time + datetime.timedelta(days=-30)
monthday = month_time.strftime('%Y%m%d')

#转换时间格式
def getday(date_time,days):
    t = time.strptime(str(date_time), "%Y%m%d")
    sjstime = datetime.datetime(t.tm_year, t.tm_mon, t.tm_mday)

    get_time = sjstime + datetime.timedelta(days=days)
    getday = get_time.strftime('%Y%m%d')
    return getday