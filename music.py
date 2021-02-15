# 生成程序
import effect as par
import os


class Track:
    """音轨类:
        - add:增加一个乐符
    """

    def __init__(self, funName='test'):
        self.pos = [0, 0, 0]
        init(funName)

    def add(self, tone, delay, effect='wujiaoxin'):
        self.newpos = [self.pos[0], self.pos[1], self.pos[2]]
        pass


def init(funName):
    """创建基础function
        - funName:函数名称
    """
    url = 'functions\\' + funName + '\\main\\' + funName
    if not os.path.exists(url):
        os.makedirs(url)
    url = 'functions\\' + funName + '\\init.mcfunction'
    with open(url, 'w') as fp:
        s = 'scoreboard objectives add ' + funName + ' dummy ' + funName
        fp.write(s)
    url = 'functions\\' + funName + '\\main.mcfunction'
    fp = open(url, 'w')
    fp.close()


newTrack = Track('a')
