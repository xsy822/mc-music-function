# mcfunction生成程序
import os
import json
import shutil
import zipfile
import effect
import routeEffect as route
import effect
# 导入同时运行mid处理文件
import midchange


def init(funName):
    url = 'xsy\\data\\xsy\\functions\\'
    if os.path.exists(url):
        shutil.rmtree(url)
    os.makedirs(url + funName+'\\main')
    url = 'xsy\\data\\xsy\\functions\\' + funName + '\\init.mcfunction'
    with open(url, 'w') as fp:
        fp.write(
            'scoreboard objectives add %s dummy "%s"\nscoreboard players set @a %s 0' % (funName, funName, funName))
    url = 'xsy\\data\\xsy\\functions\\' + funName + '\\main.mcfunction'
    fp = open(url, 'w')
    fp.close()


class Track:
    """构建音轨
        - speed:速度，单位是拍/min
        - funName:函数名
        - m为True则初始化functions目录结构，默认False
    """

    def __init__(self, speed, funName, hight, particleNum, m=False):
        self.pos = [0, hight, 0]
        self.allticks = 0
        self.mticks = 0
        self.delay = 30
        self.funName = funName
        self.speed = speed
        self.particleNum = particleNum
        if m:
            init(self.funName)

    def add(self, tone, delay, routeEffect, routeParticle, effectName, sound, btn=False):
        self.delay = delay
        newpos = [tone, self.pos[1], self.pos[2] + self.delay]
        self.allticks, self.mticks, self.pos = route.route(
            self.pos, newpos, self.speed, routeEffect, routeParticle, self.funName, effectName, tone, sound, self.allticks, self.mticks, self.particleNum, btn)


# 获取设置
with open('setting.json', 'r') as fp:
    content = fp.read()
    setting = json.loads(content)


num = setting['tracks'] if (
    midchange.num-1) > setting['tracks'] else midchange.num-1
name = midchange.fn
effectParticle = setting['effectParticle']
particleNum = setting['particleNum']


allticks = 0
sounds = []
# 读取生成音轨
for j in range(num):
    with open('%s.txt' % (name+str(j+1)), 'r') as fp:
        a = fp.read()
        a = a.split()
    funName = a[0]
    routeEffect = a[1]
    routeParticle = a[2].replace('&', ' ')
    effectName = a[3]
    sound = a[4]
    if sound not in sounds:
        sounds.append(sound)
    hight = int(a[5])
    a = a[6:]
    for index, i in enumerate(a):
        if i[0] == 'd':
            a[index-1] = 'c'+a[index-1]
    speed = int(a[0])
    a = a[1:]
    if j == 0:
        mainTrack = Track(speed, funName, hight, particleNum, m=True)
    else:
        mainTrack = Track(speed, funName, hight, particleNum)
    delay = 30
    for index, i in enumerate(a):
        print('track%d: %d/%d' % (j+1, index+1, len(a)))
        if i[0] == 'c':
            mainTrack.add(int(i[1:]), delay, routeEffect, routeParticle,
                          effectName, sound, btn=True)
        elif i[0] == 'd':
            delay = int(i[1:])
        else:
            mainTrack.add(int(i), delay, routeEffect,
                          routeParticle, effectName, sound)
    allticks = max(allticks, mainTrack.allticks)

for i in range(num):
    os.remove('%s.txt' % (name+str(i+1)))

# 配置资源包文件
if(os.path.exists('resources')):
    shutil.rmtree('resources')
os.makedirs('resources\\assets\\minecraft\\sounds')
shutil.copyfile('sounds\\pack.mcmeta', 'resources\\pack.mcmeta')
shutil.copyfile('sounds\\pack.png', 'resources\\pack.png')
shutil.copyfile('sounds\\assets\\minecraft\\sounds.json',
                'resources\\assets\\minecraft\\sounds.json')
for i in sounds:
    shutil.copytree('sounds\\assets\\minecraft\\sounds\\'+i,
                    'resources\\assets\\minecraft\\sounds\\' + i)
zip_list = []
for root, dirs, files in os.walk('resources'):
    for f in files:
        zip_list.append(os.path.join(root[10:], f))
with zipfile.ZipFile('resources.zip', 'w') as new_zip:
    for i in zip_list:
        new_zip.write('resources\\'+i, arcname=i)
shutil.rmtree('resources')

# 生成特效文件
url = 'xsy\\data\\xsy\\functions\\' + mainTrack.funName + '\\effect'
if not os.path.exists(url):
    os.makedirs(url)
effect.star(url, effectParticle)
effect.starup(url, effectParticle)
effect.square(url, effectParticle)

# 收尾
url = 'xsy\\data\\xsy\\functions\\' + mainTrack.funName + '\\main.mcfunction'
for i in range(int(allticks / 20 + 1)):
    with open(url, 'a') as fp:
        fp.write('execute as @a[scores={%s=%d..%d}] run function %s:%s/main/part%d\n' % (
            mainTrack.funName, 20*i, 20*(i + 1), 'xsy', mainTrack.funName, i))

# # 玩家传送及视角固定
for i in range(allticks):
    url = 'xsy\\data\\xsy\\functions\\%s\\main\\part%d.mcfunction' % (
        mainTrack.funName, int(i/20))
    with open(url, 'a') as fp:
        fp.write('execute as @a[scores={%s=%d}] run tp @s ~%d ~%d ~%.2f 0 50\n' %
                 (funName, i, -60, 30, i*(speed/150)-30))

url = 'xsy\\data\\xsy\\functions\\' + mainTrack.funName + '\\main.mcfunction'
with open(url, 'a') as fp:
    fp.write('scoreboard players add @a %s 1\n' % (mainTrack.funName))


print('完成！')
input('输入回车结束！')
