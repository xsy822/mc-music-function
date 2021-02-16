import effect


def route(pos, newpos, speed, routeEffect, routeParticle, funName, effectName, effectParticle, allticks, r):
    """绘制轨道路径及音符特效
        - pos:三维坐标
        - newpos:目的地坐标
        - speed:速度，单位是拍/min
        - routeEffect:路径的特效
        - routeParticle:路径粒子名称
        - funName:函数名
        - effectName:音符特效名
        - effectParticle:音符特效粒子
        - allticks:总时间，单位tick
        - r:音符特效半径
    """
    # 路线效果
    if routeEffect == 'straight':
        allticks, pos, effectpos, mainUrl = straight(
            pos, newpos, speed, routeParticle, funName, allticks)

    # 特效
    with open(mainUrl, 'a') as fp:
        if effectName == 'star':
            effect.star(funName, effectParticle, effectpos, allticks, r, fp)

    return allticks, pos


def straight(pos, newpos, speed, particle, funName, allticks):
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
    for i in range(ticks):
        for j in range(20):
            x1, z1 = x * (i * 20 + j) / (ticks * 20), z * \
                (i * 20 + j) / (ticks * 20)
            mainUrl = 'functions\\' + funName + '\\main//part' + \
                str(int(allticks/20+0.5)) + '.mcfunction'
            with open(mainUrl, 'a') as fp:
                fp.write('execute as @a[scores={%s=%d}] run particle %s ~%.2f ~%.2f ~%.2f\n' % (
                    funName, allticks, particle, x1, y, z1))
        allticks += 1
        if allticks % 20 == 0:
            url = 'functions\\' + funName + '\\main.mcfunction'
            num = int(allticks / 20)
            with open(url, 'a') as fp:
                fp.write('execute as @a[scores={%s=%d..%d}] run function a:main/part%d.mcfunction' % (
                    funName, allticks - 20, allticks, num))
    effectpos = [x1, y, z1]
    if z != 0:
        pos = effectpos
    return allticks, pos, effectpos, mainUrl


def playsound():
    pass
