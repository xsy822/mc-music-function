# 五角星特效
import math as m


def star(funName, particle, pos, time, r, fp):
    """指定地点绘制五角星
        - funName:函数名
        - particle:粒子名称
        - pos:三维坐标
        - time:时间，(计分板达到规定分数才执行)
        - r:五角星外接圆半径
        - fp:文件指针
    """
    print(pos)
    th1, th2 = 0, 360
    x, y, x1, y1, x2, y2, xc, yc = 0, 0, 0, 0, 0, 0, 0, 0
    while th1 <= 360:
        x = r * m.cos(m.radians(th1))
        y = r * m.sin(m.radians(th1))
        xc = r * 3 / 2 * m.cos(m.radians(th1)) + pos[0]
        yc = r * 3 / 2 * m.sin(m.radians(th1)) + pos[2]
        s = 'execute as @a[scores={%s=%d}] run particle %s ~%.2f ~%.2f ~%.2f ~ ~ ~ 0 0 force\n' % (
            funName, time, particle, -xc, pos[1], yc)
        fp.write(s)
        x1 = x + (r / 2) * m.cos(m.radians(th2)) + pos[0]
        y1 = y + (r / 2) * m.sin(m.radians(th2)) + pos[2]
        s = 'execute as @a[scores={%s=%d}] run particle %s ~%.2f ~%.2f ~%.2f ~ ~ ~ 0 0 force\n' % (
            funName, time, particle, -x1, pos[1], y1)
        fp.write(s)
        x2 = x + r / 2 * m.cos(m.radians(th2+180)) + pos[0]
        y2 = y + r / 2 * m.sin(m.radians(th2+180)) + pos[2]
        s = 'execute as @a[scores={%s=%d}] run particle %s ~%.2f ~%.2f ~%.2f ~ ~ ~ 0 0 force\n' % (
            funName, time, particle, -x2, pos[1], y2)
        fp.write(s)
        th1 += 6
        th2 -= 9
    fp.write('execute as @a[scores={%s=%d}] run particle %s ~%.2f ~%.2f ~%.2f ~ ~ ~ 0 500 force\n' % (
        funName, time, particle, -pos[0], pos[1], pos[2]))
