# coding:utf-8
import datetime


class DateCalculator():
    def __init__(self):
        self.today = datetime.datetime.today()  # - datetime.timedelta(days=1)
        self.now_date = self.today.strftime("%Y%m%d")


    def calculate_last_date(self, now_date, last_days):
        """
        :now_date : 开始日期
        :param last_days: 过去天数
        :return: 过去天数，那天的日期
        """
        if not now_date:
            now_date = self.today
        last_date = (now_date - datetime.timedelta(days=last_days)).strftime("%Y%m%d")
        return last_date

    def str_to_date(self, date_str, format= '%Y%m%d'):
        """
        字符串转日期
        :param date_str: 字符串格式的日期
        : format: 格式 默认 '%Y%m%d'
        :return: 
        """
        return datetime.datetime.strptime(date_str,format)

    def gen_dates(self, b_date, days):
        day = datetime.timedelta(days=1)
        for i in range(days):
            yield b_date + day * i

    def get_date_list(self, start=None, end=None):
        """
        获取日期列表
        :param start: 开始日期
        :param end: 结束日期
        :return:
        """
        if start is None:
            start = datetime.datetime.strptime("2000-01-01", "%Y-%m-%d")
        else:
            start = datetime.datetime.strptime(start, "%Y%m%d")
        if end is None:
            end = datetime.datetime.now()
        else:
            end = datetime.datetime.strptime(end, "%Y%m%d")
        data = []
        for d in self.gen_dates(start, (end - start).days):
            data.append(d.strftime("%Y%m%d"))
        return data

    def get_week(self, date):
        date_time = self.str_to_date(date)
        return date_time.weekday()

if __name__ == '__main__':
    dc = DateCalculator()
    aa = dc.calculate_last_date(None,1)
    print(aa)

