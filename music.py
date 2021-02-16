# 生成程序
# 结构乱七八糟，参数乱传，写的垃圾代码
import os

import effect
import routeEffect as route


class Track:
    """构建新工程
        - speed:速度，单位是拍/min
        - funName:函数名
        - routeEffect:路径的特效
        - routeParticle:路径粒子名称
    """

    def __init__(self, speed, funName='test', routeEffect='straight', routeParticle='flame'):
        self.pos = [0, 0, 0]
        self.funName = funName
        self.speed = speed
        self.routeEffect = routeEffect
        self.routeParticle = routeParticle
        self.allticks = 0
        init(self.funName)

    def add(self, tone, delay, effectName='star', effectParticle='flame', r=2):
        """增加一个音符
            - tone:音调，降1开始的递增数(1,2,3...)
            - delay:上一个与下一个音符间的间隔，单位1/32全音符
            - effectName:音符特效名(默认'star')
            - effectParticle:音符特效粒子(默认'flame')
            - r:特效半径(默认2)
        """
        self.newpos = [tone, self.pos[1], self.pos[2]+delay]
        self.allticks, self.pos = route.route(self.pos, self.newpos, self.speed, self.routeEffect,
                                              self.routeParticle, self.funName, effectName, effectParticle, self.allticks, r)


def init(funName):
    """创建基础function文件夹路径
        - funName:函数名称
    """
    url = 'functions\\' + funName + '\\main'
    if not os.path.exists(url):
        os.makedirs(url)
    url = 'functions\\' + funName + '\\init.mcfunction'
    with open(url, 'w') as fp:
        fp.write(
            'scoreboard objectives add %s dummy "%s"\nscoreboard players set @a %s 0' % (funName, funName, funName))
    url = 'functions\\' + funName + '\\main.mcfunction'
    fp = open(url, 'w')
    fp.close()


newTrack = Track(90, 'star')  # test
newTrack.add(1, 3)
newTrack.add(2, 3)
if newTrack.allticks % 20:
    url = 'functions\\' + newTrack.funName + '\\main.mcfunction'
    num = int(newTrack.allticks / 20)
    with open(url, 'a') as fp:
        fp.write('execute as @a[scores={%s=%d..%d}] run function a:main/part%d.mcfunction\n' % (
            newTrack.funName, 20*num, 20*(num+1), num))
