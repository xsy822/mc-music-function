# mc-music-function

**根据指定格式文本乐谱生成 mc 粒子音乐 function 包**

---

mc-music-function 1.0
2021/2/18 23:13
正式完成，测试通过

## 文档

### 文件结构

- `_pycache_` _(编译得到的 py 程序，effect.py 和 routeEffect.py，运行程序自动产生的)_
- functions _(生成的 function 包，没有这个文件夹运行此程序也会自动产生)_
  - star _(根据函数名生成的文件夹)_
    - main
      - part0.mcfunction _(主要效果实现)_
      - ...
    - init.mcfunction _(初始化计分板)_
    - main.mcfunction _(增加计分用于计时及调用其他 function 的主干)_
- sounds _(音色资源包，必须有这个才能用本 function，音色资源出自 soma，由小世炎修改，节选适配本程序及 mc 1.13 以后版本)[资源包相关内容查看 mcwiki](https://minecraft-zh.gamepedia.com/%E8%B5%84%E6%BA%90%E5%8C%85)_
- effect.py _(音符特效的支持文件)_
- music.py _(此程序主要文件（入口），使用此程序即运行本文件)_
- README.md
- routeEffect.py _(路径特效，例如直线等，主程序的支持)_
- musics _(存放乐谱，注：乐谱使用要与程序同级)_
  - star1.txt _(乐谱 1，一首乐曲由多条音轨组成，一个乐谱即一条音轨)_
  - star2.txt _(乐谱 2)_
  - ...

### 使用

#### 乐谱格式

多个乐谱格式须相同，文件名统一为 名字+数字+.txt ，如：star1.txt
乐谱内容由声明和乐谱组成，用(任意)空白符隔开
声明内容为：

1. funName _(函数名，须统一)_
1. routeEffect _(路径特效)_
1. routeParticle _(路径粒子名称)_
1. effectName _(音符特效)_
1. effectParticle _(音符特效粒子名称)_
1. sound _(音色代码)_
1. speed _(速度，拍/min)_

乐谱：
由音调与延迟(当前与下一音调的间隔，单位是 1/32 音符，没有（下一个音符和当前同时）不填)组成
音调：0-127 对应 128 个半音，中央 c 为 60

示例请看附带的乐谱

#### 一些代码

routeEffect

- straight _(**直线**，目前仅有)_

effectName

- star _(**五芒星阵**，目前仅有)_

sound

- 0 _(**古典钢琴**，目前仅有)_

粒子名称，[参考 mcwiki/particle](https://minecraft-zh.gamepedia.com/%E5%91%BD%E4%BB%A4/particle)
若粒子名称中带有参数，如 `dust 1.0 0.5 0.5 1.0`
请不要用空格间隔，应替换为`&`，如 `dust&1.0&0.5&0.5&1.0`

#### 注意

**要使用 function 包，需要保证 function 命名空间和 funName 一致**
[参考 mcwiki/function](https://minecraft-zh.gamepedia.com/%E5%91%BD%E4%BB%A4/function)
