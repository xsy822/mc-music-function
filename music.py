# 生成程序
# 结构乱七八糟，参数乱传，写的垃圾代码
import os

import effect
import routeEffect as route


class Track:
    """构建音轨
        - speed:速度，单位是拍/min
        - funName:函数名
        - m为True则初始化functions目录结构，默认False
    """

    def __init__(self, speed, funName, m=False):
        self.pos = [0, 0, 0]
        self.allticks = 0
        self.mticks = 0
        self.delay = 30
        self.funName = funName
        self.speed = speed
        if m:
            init(self.funName)

    def add(self, tone, delay, routeEffect, routeParticle, effectName, effectParticle, sound,  r=1, btn=False):
        """增加一个音符
            - tone:音调，降1开始的递增数(1,2,3...)
            - delay:上一个与下一个音符间的间隔，单位1/32全音符
            - routeEffect:路线特效
            - routeParticle:路线粒子效果
            - effectName:音符特效名
            - effectParticle:音符特效粒子
            - sound:音色编号
            - r:特效半径(默认1)
            - btn:是否切换下一拍
        """
        if btn:
            self.delay = delay
        newpos = [tone, self.pos[1], self.pos[2] + self.delay]
        self.allticks, self.mticks, self.pos = route.route(self.pos, newpos, self.speed, routeEffect, routeParticle,
                                                           self.funName, effectName, effectParticle, tone, sound, self.allticks, self.mticks, r, btn)
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


num = int(input('音轨数量：'))
name = input('输入文件名：')
allticks = 0
for j in range(num):
    with open('%s.txt' % (name+str(j+1)), 'r') as fp:
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
    if j == 0:
        mainTrack = Track(speed, funName, m=True)
    else:
        mainTrack = Track(speed, funName)
    delay = 30
    for i in a:
        if i[0] == 'c':
            mainTrack.add(int(i[1:]), delay, routeEffect, routeParticle,
                          effectName, effectParticle, sound, btn=True)
        elif i[0] == 'd':
            delay = int(i[1:])
        else:
            mainTrack.add(int(i), delay, routeEffect, routeParticle,
                          effectName, effectParticle, sound)
    allticks = max(allticks, mainTrack.allticks)


# 收尾
url = 'functions\\' + mainTrack.funName + '\\main.mcfunction'
for i in range(int(allticks / 20 + 1)):
    with open(url, 'a') as fp:
        fp.write('execute as @a[scores={%s=%d..%d}] run function %s:%s/main/part%d\n' % (
            mainTrack.funName, 20*i, 20*(i + 1), mainTrack.funName, mainTrack.funName, i))

# 玩家传送及视角固定
for i in range(allticks):
    url = 'functions\\%s\\main\\part%d.mcfunction' % (
        mainTrack.funName, int(i/20))
    with open(url, 'a') as fp:
        fp.write('execute as @a[scores={%s=%d}] run tp @s ~%d ~%d ~%.2f 0 40\n' %
                 (funName, i, -60, 15, i*(speed/150)-20))

url = 'functions\\' + mainTrack.funName + '\\main.mcfunction'
with open(url, 'a') as fp:
    fp.write('scoreboard players add @a %s 1\n' % (mainTrack.funName))
