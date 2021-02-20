import effect


def route(pos, newpos, speed, routeEffect, routeParticle, funName, effectName, effectParticle, tone, sound, allticks, mticks, r, btn):
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

    # 特效
    with open(mainUrl, 'a') as fp:
        if effectName == 'star':
            effect.star(funName, effectParticle, effectpos, effectTicks, r, fp)

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
        for j in range(20):
            x1, z1 = round(pos[0] + x * (i * 20 + j) / (ticks * 20),
                           2), round(pos[2] + z * (i * 20 + j) / (ticks * 20), 2)
            mainUrl = 'functions\\' + funName + '\\main\\part' + \
                str(int(allticks/20)) + '.mcfunction'
            with open(mainUrl, 'a') as fp:
                fp.write('execute as @a[scores={%s=%d}] run particle %s ~%.2f ~%.2f ~%.2f ~ ~ ~ 0 0 force\n' % (
                    funName, allticks, particle, -x1, y, z1))
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
