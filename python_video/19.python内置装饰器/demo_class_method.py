class DateFormat:
    def __init__(self, year=0, month=0, day=0):
        self.year = year
        self.month = month
        self.day = day

    def out_date(self):
        return f"输入的时间为{self.year}年，{self.month}月，{self.day}日"

    @classmethod
    def json_format(cls, json_data):
        """
        输入一个字典格式的数据信息，返回 (2021, 1, 2)
        """
        year, month, day = json_data["year"], json_data["month"], json_data["day"]
        # return cls(year, month, day)
        return cls(year, month, day)

    @classmethod
    def str_format(self):
        return



json_date = {"year": 2021, "month": 12, "day": 24}
# 使用json格式化，生成想要的日期格式，返回DateFormat实例
demo = DateFormat.json_format(json_date)
print(demo.out_date())


#
# def json_format(json_data):
#     year, month, day = json_data["year"], json_data["month"], json_data["day"]
#     # print(year, month, day)
#     return year, month, day
#
# def str_format(str):
#     return
#
# print(json_format({"year": 2021, "month": 12, "day": 24}))
# year, month, day = json_format({"year": 2021, "month": 12, "day": 24})
#