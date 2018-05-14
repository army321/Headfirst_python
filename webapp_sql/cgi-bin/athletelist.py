
class AthleteList(list):

    def __init__(self, a_name, a_dob=None, a_times=[]): 
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)

    @staticmethod
    def sanitize(time_string):  #把数据切分开，原始的数据分为3个部分，名字，出生日期和多次的成绩
        if '-' in time_string:
            splitter = '-'
        elif ':' in time_string:
            splitter = ':'
        else:
            return(time_string)
        (mins, secs) = time_string.split(splitter)
        return(mins + '.' + secs)

    @property
    def top3(self):  #提取最好的3个成绩
        return(sorted(set([self.sanitize(t) for t in self]))[0:3])  #包含多个内容：分段，排序，提取前几个数量，

    @property
    def clean_data(self):
        return(sorted(set([self.sanitize(t) for t in self])))  #清理数据
