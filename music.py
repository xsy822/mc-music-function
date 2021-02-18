# 生成程序
# 结构乱七八糟，参数乱传，写的垃圾代码
import os

import effect
import routeEffect as route


class Track:
    """构建音轨
        - speed:速度，单位是拍/min
        - funName:函数名
        - routeEffect:路径的特效
        - routeParticle:路径粒子名称
    """

    def __init__(self, speed, funName, m=False):
        self.pos = [0, 0, 0]
        self.allticks = 0
        self.delay = 10
        self.funName = funName
        self.speed = speed
        if m:
            init(self.funName)

    def add(self, tone, delay, routeEffect, routeParticle, effectName, effectParticle, sound,  r=1, m=False, btn=False):
        """增加一个音符
            - tone:音调，降1开始的递增数(1,2,3...)
            - delay:上一个与下一个音符间的间隔，单位1/32全音符
            - effectName:音符特效名
            - effectParticle:音符特效粒子
            - r:特效半径(默认1)
            - m:标记区别伴奏
            - btn:是否切换下一拍
        """
        if btn:
            self.delay = delay
        newpos = [tone, self.pos[1], self.pos[2] + self.delay]
        self.allticks, self.pos = route.route(self.pos, newpos, self.speed, routeEffect, routeParticle,
                                              self.funName, effectName, effectParticle, tone, sound, self.allticks, r, m, btn)
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


# 主旋律
name = 'star1'
with open('%s.txt' % (name), 'r') as fp:
    a = fp.read()
    a = a.split()
    funName = a[0]
    routeEffect = a[1]
    routeParticle = a[2].replace('&', ' ')
    effectName = a[3]
    effectParticle = a[4].replace('&', ' ')
    sound = int(a[5])
    a = a[6:]
    for index, i in enumerate(a):
        if i[0] == 'd':
            a[index-1] = 'c'+a[index-1]
    speed = int(a[0])
    print(a)
    a = a[1:]

mainTrack = Track(speed, funName, True)
delay = 10
for i in a:
    if i[0] == 'c':
        mainTrack.add(int(i[1:]), delay, routeEffect, routeParticle,
                      effectName, effectParticle, sound, m=True, btn=True)
    elif i[0] == 'd':
        delay = int(i[1:])
    else:
        mainTrack.add(int(i), delay, routeEffect, routeParticle,
                      effectName, effectParticle, sound, m=True)


# 伴奏
name = 'star2'
with open('%s.txt' % (name), 'r') as fp:
    a = fp.read()
    a = a.split()
    funName = a[0]
    routeEffect = a[1]
    routeParticle = a[2].replace('&', ' ')
    effectName = a[3]
    effectParticle = a[4].replace('&', ' ')
    sound = int(a[5])
    a = a[6:]
    for index, i in enumerate(a):
        if i[0] == 'd':
            a[index-1] = 'c'+a[index-1]
    speed = int(a[0])
    print(speed)
    a = a[1:]

assistantTrack = Track(speed, name[:-1])
delay = 10
for i in a:
    if i[0] == 'c':
        assistantTrack.add(int(i[1:]), delay, routeEffect, routeParticle,
                           effectName, effectParticle, sound, btn=True)
    elif i[0] == 'd':
        delay = int(i[1:])
    else:
        assistantTrack.add(int(i), delay, routeEffect, routeParticle,
                           effectName, effectParticle, sound)


# 收尾
allticks = max(mainTrack.allticks, assistantTrack.allticks)
url = 'functions\\' + mainTrack.funName + '\\main.mcfunction'
for i in range(int(allticks / 20 + 2)):
    with open(url, 'a') as fp:
        fp.write('execute as @a[scores={%s=%d..%d}] run function %s:%s/main/part%d\n' % (
            mainTrack.funName, 20*i, 20*(i + 1), mainTrack.funName, mainTrack.funName, i))

with open(url, 'a') as fp:
    fp.write('scoreboard players add @a %s 1\n' % (mainTrack.funName))
