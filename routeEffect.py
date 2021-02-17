import effect


def route(pos, newpos, speed, routeEffect, routeParticle, funName, effectName, effectParticle, tone, sound, allticks, r, m, btn):
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
        - sound:音色
        - allticks:总时间，单位tick
        - r:音符特效半径
        - btn:判断是否为同一拍的乐符
    """
    # 路线效果
    if routeEffect == 'straight':
        allticks, effectTicks, pos, effectpos, mainUrl = straight(
            pos, newpos, speed, routeParticle, funName, allticks, m, btn)

    # 特效
    with open(mainUrl, 'a') as fp:
        if effectName == 'star':
            effect.star(funName, effectParticle, effectpos, effectTicks, r, fp)

    # 音色
    with open(mainUrl, 'a') as fp:
        playsound(funName, effectpos, sound, tone, effectTicks, fp)

    return allticks, pos


def straight(pos, newpos, speed, particle, funName, allticks, m, btn):
    """直线
        - pos:三维坐标
        - newpos:目的地坐标
        - speed:速度，单位是拍/min
        - particle:路径粒子名称
        - funName:函数名
        - allticks:总时间，单位tick
    """
    x, y, z = [i - j for i, j in zip(newpos, pos)]
    if m:
        x += 7
    ticks = int((z * 300) / (speed * 2) + 0.5)
    for i in range(ticks):
        for j in range(20):
            x1, z1 = round(pos[0] + x * (i * 20 + j) / (ticks * 20),
                           2), round(pos[2] + z * (i * 20 + j) / (ticks * 20), 2)
            mainUrl = 'functions\\' + funName + '\\main//part' + \
                str(int(allticks/20)) + '.mcfunction'
            with open(mainUrl, 'a') as fp:
                fp.write('execute as @a[scores={%s=%d}] run particle %s ~%.2f ~%.2f ~%.2f\n' % (
                    funName, allticks, particle, -x1, y, z1))
        allticks += 1
    effectpos = [x1, y, z1]
    effectTicks = allticks
    if btn:
        pos = effectpos
    else:
        allticks -= ticks
    return allticks, effectTicks, pos, effectpos, mainUrl


def playsound(funName, effectpos, sound, tone, allticks, fp):
    music = {5: 0.530, 6: 0.595, 7: 0.667, 8: 0.707, 9: 0.794,
             10: 0.890, 11: 0.944, 12: 1.059, 13: 1.189, 14: 1.334, 15: 1.414, 16: 1.587, 17: 1.781, 18: 1.888}
    tone = music[tone]
    fp.write('execute as @a[scores={%s=%d}] at @s run playsound minecraft:block.note_block.%s master @a ~ ~ ~ 1 %.3f\n' % (
        funName, allticks, sound, tone))
