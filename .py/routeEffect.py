import random
import math
import effect


def route(pos, newpos, speed, routeEffect, routeParticle, funName, effectName, tone, sound, allticks, mticks, particleNum, velocity, btn):
    # 路线效果
    if routeEffect == 'straight':
        allticks, mticks, effectTicks, pos, effectpos = straight(
            pos, newpos, speed, routeParticle, funName, allticks, mticks, particleNum, btn)
    if routeEffect == 'oval':
        allticks, mticks, effectTicks, pos, effectpos = oval(
            pos, newpos, speed, routeParticle, funName, allticks, mticks, particleNum, btn)
    if routeEffect == 'brokenLine':
        allticks, mticks, effectTicks, pos, effectpos = brokenLine(
            pos, newpos, speed, routeParticle, funName, allticks, mticks, particleNum, btn)

    # 特效
    num = int(effectTicks/20)
    url = 'xsy\\data\\xsy\\functions\\%s\\main\\part%d.mcfunction' % (
        funName, num)
    with open(url, 'a') as fp:
        fp.write('execute as @a[scores={%s=%d}] positioned ~%.2f ~%.2f ~%.2f run function xsy:%s/effect/%s\n' % (
            funName, effectTicks, -effectpos[0], effectpos[1], effectpos[2], funName, effectName))

    # 音色
    num = int(effectTicks/20)
    url = 'xsy\\data\\xsy\\functions\\%s\\main\\part%d.mcfunction' % (
        funName, num)
    with open(url, 'a') as fp:
        playsound(funName, sound, tone, velocity, effectTicks, fp)

    return allticks, mticks, pos


def straight(pos, newpos, speed, particle, funName, allticks, mticks, particleNum, btn):
    """直线
        - pos:三维坐标
        - newpos:目的地坐标
        - speed:速度，单位是拍/min
        - particle:路径粒子名称
        - funName:函数名
        - allticks:总时间，单位tick
    """
    initallticks = allticks
    initmticks = mticks
    x, y, z = [i - j for i, j in zip(newpos, pos)]
    ticks = int((z * 300) / (speed * 2) + 0.5)
    mticks += (z * 300) / (speed * 2) - ticks
    if mticks <= -1:
        allticks -= 1
        mticks += 1
    elif mticks >= 1:
        allticks += 1
        mticks -= 1
    for i in range(ticks):
        for j in range(particleNum):
            x1, z1 = round(pos[0] + x * (i * particleNum + j) / (ticks * particleNum),
                           2), round(pos[2] + z * (i * particleNum + j) / (ticks * particleNum), 2)
            url = 'xsy\\data\\xsy\\functions\\' + funName + '\\main\\part' + \
                str(int(allticks/20)) + '.mcfunction'
            with open(url, 'a') as fp:
                fp.write('execute as @a[scores={%s=%d}] run particle %s ~%.2f ~%.2f ~%.2f ~ ~ ~ 0 0 force\n' % (
                    funName, allticks, particle, -x1, y+pos[1], z1))
        allticks += 1
    effectpos = newpos
    effectTicks = allticks
    if btn:
        pos = effectpos
    else:
        allticks = initallticks
        mticks = initmticks
    return allticks, mticks, effectTicks, pos, effectpos


def oval(pos, newpos, speed, particle, funName, allticks, mticks, particleNum, btn):
    """椭圆线
    """
    initallticks = allticks
    initmticks = mticks
    x, y, z = [i - j for i, j in zip(newpos, pos)]
    ticks = int((z * 300) / (speed * 2) + 0.5)
    mticks += (z * 300) / (speed * 2) - ticks
    if mticks <= -1:
        allticks -= 1
        mticks += 1
    elif mticks >= 1:
        allticks += 1
        mticks -= 1
    b = (((x * x) + (z * z))**(1 / 2)) / 2
    if x == 0:
        th = math.radians(90)
    else:
        th = math.atan(z / abs(x))
        if x < 0:
            th = math.pi-th
    for i in range(ticks):
        for j in range(particleNum):
            th2 = math.radians((i * particleNum + j) /
                               (ticks * particleNum) * 180 - 90)
            y = 2 * b * math.cos(th2)
            p = b * math.sin(th2) + b
            x = p * math.cos(th)
            z = p * math.sin(th)
            url = 'xsy\\data\\xsy\\functions\\' + funName + '\\main\\part' + \
                str(int(allticks/20)) + '.mcfunction'
            with open(url, 'a') as fp:
                fp.write('execute as @a[scores={%s=%d}] run particle %s ~%.2f ~%.2f ~%.2f ~ ~ ~ 0 0 force\n' % (
                    funName, allticks, particle, -(x+pos[0]), y+pos[1], z+pos[2]))
        allticks += 1
    effectpos = newpos
    effectTicks = allticks
    if btn:
        pos = effectpos
    else:
        allticks = initallticks
        mticks = initmticks
    return allticks, mticks, effectTicks, pos, effectpos


def brokenLine(pos, newpos, speed, particle, funName, allticks, mticks, particleNum, btn):
    """折线
    """
    initallticks = allticks
    initmticks = mticks
    x, y, z = [i - j for i, j in zip(newpos, pos)]
    ticks = int((z * 300) / (speed * 2) + 0.5)
    mticks += (z * 300) / (speed * 2) - ticks
    if mticks <= -1:
        allticks -= 1
        mticks += 1
    elif mticks >= 1:
        allticks += 1
        mticks -= 1
    for i in range(ticks):
        for j in range(particleNum):
            x1, z1 = round(pos[0] + x * (i * particleNum + j) / (ticks * particleNum),
                           2), round(pos[2] + z*(i * particleNum + j) / (ticks * particleNum), 2)
            y = 4 * (i * particleNum + j) / (ticks * particleNum)
            if y >= 2:
                y = 4-y
            url = 'xsy\\data\\xsy\\functions\\' + funName + '\\main\\part' + \
                str(int(allticks/20)) + '.mcfunction'
            with open(url, 'a') as fp:
                fp.write('execute as @a[scores={%s=%d}] run particle %s ~%.2f ~%.2f ~%.2f ~ ~ ~ 0 0 force\n' % (
                    funName, allticks, particle, -x1, y + pos[1], z1))
                fp.write('execute as @a[scores={%s=%d}] run particle %s ~%.2f ~%.2f ~%.2f ~ ~ ~ 0 0 force\n' % (
                    funName, allticks, particle, -x1, -y + pos[1], z1))
        allticks += 1
    effectpos = newpos
    effectTicks = allticks
    if btn:
        pos = effectpos
    else:
        allticks = initallticks
        mticks = initmticks
    return allticks, mticks, effectTicks, pos, effectpos


def playsound(funName, sound, tone, velocity, allticks, fp):
    """播放声音
    - funName:函数名
    - sound: 音色编号
    - tone:音调
    - allticks:播放声音的时刻
    - fp:写入位置指针
    """
    fp.write('execute as @a[scores={%s=%d}] at @s run playsound %s.%d master @a ~ ~ ~ %lf\n' % (
        funName, allticks, sound, tone, velocity))
