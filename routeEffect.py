import random
import math
import effect


def route(pos, newpos, speed, routeEffect, routeParticle, funName, effectName, effectParticle, tone, sound, allticks, mticks, block, r, btn):
    """绘制轨道路径及音符特效
        - pos:三维坐标
        - newpos:目的地坐标
        - speed:速度，单位是拍/min
        - routeEffect:路径的特效
        - routeParticle:路径粒子名称
        - funName:函数名
        - effectName:音符特效名
        - effectParticle:音符特效粒子
        - tone:音调
        - sound:音色编号
        - allticks:总时间，单位tick
        - mticks:用于减小误差的附加值
        - r:音符特效半径
        - btn:判断是否为同一拍的乐符
    """
    # 路线效果
    if routeEffect == 'straight':
        allticks, mticks, effectTicks, pos, effectpos, mainUrl = straight(
            pos, newpos, speed, routeParticle, funName, allticks, mticks, btn)
    if routeEffect == 'oval':
        allticks, mticks, effectTicks, pos, effectpos, mainUrl = oval(
            pos, newpos, speed, routeParticle, funName, allticks, mticks, btn)
    if routeEffect == 'brokenLine':
        allticks, mticks, effectTicks, pos, effectpos, mainUrl = brokenLine(
            pos, newpos, speed, routeParticle, funName, allticks, mticks, btn)

    # 特效
    if effectName == 'star':
        effect.star(funName, effectParticle,
                    effectpos, effectTicks, block, r)
    elif effectName == 'starUp':
        effect.starUp(funName, effectParticle,
                      effectpos, effectTicks, block, r)
    elif effectName == 'square':
        effect.square(funName, effectParticle,
                      effectpos, effectTicks, block, r)

    # 音色
    with open(mainUrl, 'a') as fp:
        playsound(funName, sound, tone, effectTicks, fp)

    return allticks, mticks, pos


def straight(pos, newpos, speed, particle, funName, allticks, mticks, btn):
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
        for j in range(10):
            x1, z1 = round(pos[0] + x * (i * 10 + j) / (ticks * 10),
                           2), round(pos[2] + z * (i * 10 + j) / (ticks * 10), 2)
            mainUrl = 'xsy\\data\\xsy\\functions\\' + funName + '\\main\\part' + \
                str(int(allticks/20)) + '.mcfunction'
            with open(mainUrl, 'a') as fp:
                fp.write('execute as @a[scores={%s=%d}] run particle %s ~%.2f ~%.2f ~%.2f ~ ~ ~ 0 0 force\n' % (
                    funName, allticks, random.choice(particle), -x1, y, z1))
        allticks += 1
    effectpos = newpos
    effectTicks = allticks
    if btn:
        pos = effectpos
    else:
        allticks = initallticks
        mticks = initmticks
    return allticks, mticks, effectTicks, pos, effectpos, mainUrl


def oval(pos, newpos, speed, particle, funName, allticks, mticks, btn):
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
        for j in range(10):
            th2 = math.radians((i * 10 + j) / (ticks * 10) * 180 - 90)
            y = 2 * b * math.cos(th2)
            p = b * math.sin(th2) + b
            x = p * math.cos(th)
            z = p * math.sin(th)
            mainUrl = 'xsy\\data\\xsy\\functions\\' + funName + '\\main\\part' + \
                str(int(allticks/20)) + '.mcfunction'
            with open(mainUrl, 'a') as fp:
                fp.write('execute as @a[scores={%s=%d}] run particle %s ~%.2f ~%.2f ~%.2f ~ ~ ~ 0 0 force\n' % (
                    funName, allticks, random.choice(particle), -(x+pos[0]), y+pos[1], z+pos[2]))
        allticks += 1
    effectpos = newpos
    effectTicks = allticks
    if btn:
        pos = effectpos
    else:
        allticks = initallticks
        mticks = initmticks
    return allticks, mticks, effectTicks, pos, effectpos, mainUrl


def brokenLine(pos, newpos, speed, particle, funName, allticks, mticks, btn):
    """折线
    """
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
        for j in range(10):
            x1, z1 = round(pos[0] + x * (i * 10 + j) / (ticks * 10),
                           2), round(pos[2] + z*(i * 10 + j) / (ticks * 10), 2)
            y = 4 * (i * 10 + j) / (ticks * 10)
            if y >= 2:
                y = 4-y
            mainUrl = 'xsy\\data\\xsy\\functions\\' + funName + '\\main\\part' + \
                str(int(allticks/20)) + '.mcfunction'
            with open(mainUrl, 'a') as fp:
                fp.write('execute as @a[scores={%s=%d}] run particle %s ~%.2f ~%.2f ~%.2f ~ ~ ~ 0 0 force\n' % (
                    funName, allticks, random.choice(particle), -x1, y + pos[1], z1))
                fp.write('execute as @a[scores={%s=%d}] run particle %s ~%.2f ~%.2f ~%.2f ~ ~ ~ 0 0 force\n' % (
                    funName, allticks, random.choice(particle), -x1, -y + pos[1], z1))
        allticks += 1
    effectpos = newpos
    effectTicks = allticks
    if btn:
        pos = effectpos
    else:
        allticks -= ticks
    return allticks, mticks, effectTicks, pos, effectpos, mainUrl


def playsound(funName, sound, tone, allticks, fp):
    """播放声音
    - funName:函数名
    - sound: 音色编号
    - tone:音调
    - allticks:播放声音的时刻
    - fp:写入位置指针
    """
    fp.write('execute as @a[scores={%s=%d}] at @s run playsound %d.%d master @a ~ ~ ~\n' % (
        funName, allticks, sound, tone))
