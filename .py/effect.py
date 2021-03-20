import math as m


def star(url, particle, r=1):
    th1, th2 = 0, 360
    url = url+'\\star.mcfunction'
    with open(url, 'w') as fp:
        fp.write('')
    with open(url, 'a') as fp:
        while th1 <= 360:
            x = r * m.cos(m.radians(th1))
            y = r * m.sin(m.radians(th1))
            xc = r * 3 / 2 * m.cos(m.radians(th1))
            yc = r * 3 / 2 * m.sin(m.radians(th1))
            a = ((xc ** 2) + (yc ** 2)) ** (1 / 2)
            xd = xc / a
            yd = yc / a
            s = 'particle %s ~%.2f ~%.2f ~%.2f %.2f 0 %.2f 0.2 0 force\n' % (
                particle, -xc, 0, yc, -xd, yd)
            fp.write(s)
            x1 = x + (r / 2) * m.cos(m.radians(th2))
            y1 = y + (r / 2) * m.sin(m.radians(th2))
            a = ((x1 ** 2) + (y1 ** 2)) ** (1 / 2)
            xd = x1 / a
            yd = y1 / a
            s = 'particle %s ~%.2f ~%.2f ~%.2f %.2f 0 %.2f 0.2 0 force\n' % (
                particle, -x1, 0, y1, -xd, yd)
            fp.write(s)
            x2 = x + r / 2 * m.cos(m.radians(th2+180))
            y2 = y + r / 2 * m.sin(m.radians(th2 + 180))
            a = ((x2 ** 2) + (y2 ** 2)) ** (1 / 2)
            xd = x2 / a
            yd = y2 / a
            s = 'particle %s ~%.2f ~%.2f ~%.2f %.2f 0 %.2f 0.2 0 force\n' % (
                particle, -x2, 0, y2, -xd, yd)
            fp.write(s)
            th1 += 6
            th2 -= 9


def starup(url, particle, r=1):
    th1, th2 = 0, 360
    url = url+'\\starup.mcfunction'
    with open(url, 'w') as fp:
        fp.write('')
    with open(url, 'a') as fp:
        while th1 <= 360:
            x = r * m.cos(m.radians(th1))
            y = r * m.sin(m.radians(th1))
            xc = r * 3 / 2 * m.cos(m.radians(th1))
            yc = r * 3 / 2 * m.sin(m.radians(th1))
            a = ((xc ** 2) + (yc ** 2)) ** (1 / 2)
            xd = xc / a
            yd = yc / a
            s = 'particle %s ~%.2f ~%.2f ~%.2f 0 3 0 0.1 0 force\n' % (
                particle, -xc, 0, yc)
            fp.write(s)
            x1 = x + (r / 2) * m.cos(m.radians(th2))
            y1 = y + (r / 2) * m.sin(m.radians(th2))
            a = ((x1 ** 2) + (y1 ** 2)) ** (1 / 2)
            xd = x1 / a
            yd = y1 / a
            s = 'particle %s ~%.2f ~%.2f ~%.2f 0 3 0 0.1 0 force\n' % (
                particle, -x1, 0, y1)
            fp.write(s)
            x2 = x + r / 2 * m.cos(m.radians(th2+180))
            y2 = y + r / 2 * m.sin(m.radians(th2 + 180))
            a = ((x2 ** 2) + (y2 ** 2)) ** (1 / 2)
            xd = x2 / a
            yd = y2 / a
            s = 'particle %s ~%.2f ~%.2f ~%.2f 0 3 0 0.1 0 force\n' % (
                particle, -x2, 0, y2)
            fp.write(s)
            th1 += 6
            th2 -= 9


def square(url, particle):
    url = url+'\\square.mcfunction'
    with open(url, 'w') as fp:
        fp.write('')
    with open(url, 'a') as fp:
        for x in [0, 2]:
            for y in [0, 2]:
                for z in range(20):
                    fp.write('particle %s ~%.2f ~%.2f ~%.2f 0 3 0 0.1 0 force\n' %
                             (particle, -(x - 1), y - 1, (z / 10) - 1))
        for y in [0, 2]:
            for z in [0, 2]:
                for x in range(20):
                    fp.write('particle %s ~%.2f ~%.2f ~%.2f 0 3 0 0.1 0 force\n' %
                             (particle, -((x / 10) - 1), y - 1, + z - 1))
        for x in [0, 2]:
            for z in [0, 2]:
                for y in range(20):
                    fp.write('particle %s ~%.2f ~%.2f ~%.2f 0 3 0 0.1 0 force\n' %
                             (particle, -(x - 1), (y / 10) - 1,  z - 1))
