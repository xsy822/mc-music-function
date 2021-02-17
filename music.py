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
        self.allticks = 0
        self.delay = 10
        self.funName = funName
        self.speed = speed
        self.routeEffect = routeEffect
        self.routeParticle = routeParticle
        init(self.funName)

    def add(self, tone, delay, effectName='star', effectParticle='flame', r=2, sound='harp', btn=False):
        """增加一个音符
            - tone:音调，降1开始的递增数(1,2,3...)
            - delay:上一个与下一个音符间的间隔，单位1/32全音符
            - effectName:音符特效名(默认'star')
            - effectParticle:音符特效粒子(默认'flame')
            - r:特效半径(默认2)
            - btn:是否切换下一拍
        """
        if btn:
            self.delay = delay
        newpos = [tone, self.pos[1], self.pos[2] + self.delay]
        self.allticks, self.pos = route.route(self.pos, newpos, self.speed, self.routeEffect, self.routeParticle,
                                              self.funName, effectName, effectParticle, tone, sound, self.allticks, r, btn)
        print(self.pos)


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


# 主要部分
name = 'star'
with open('%s.txt' % (name), 'r') as fp:
    a = fp.read()
    a = a.split()
    for index, i in enumerate(a):
        if i[0] == 'd':
            a[index-1] = 'c'+a[index-1]
    speed = int(a[0])
    a = a[1:]

newTrack = Track(speed, name)
delay = 10
for i in a:
    if i[0] == 'c':
        if i[1] == 'A':
            newTrack.add(int(i[2:]), delay, btn=True)
        else:
            newTrack.add(int(i[1:]), delay, sound='guitar', btn=True)
    elif i[0] == 'd':
        delay = int(i[1])
    else:
        if i[0] == 'A':
            newTrack.add(int(i[1:]), delay)
        else:
            newTrack.add(int(i), delay, sound='guitar')

# 收尾
url = 'functions\\' + newTrack.funName + '\\main.mcfunction'
for i in range(int(newTrack.allticks / 20 + 2)):
    with open(url, 'a') as fp:
        fp.write('execute as @a[scores={%s=%d..%d}] run function %s:%s/main/part%d\n' % (
            newTrack.funName, 20*i, 20*(i + 1), newTrack.funName, newTrack.funName, i))

with open(url, 'a') as fp:
    fp.write('scoreboard players add @a %s 1\n' % (newTrack.funName))
