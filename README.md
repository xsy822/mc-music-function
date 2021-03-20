# mc-music-function

**根据指定格式文本乐谱生成 mc 粒子音乐 function 包**

---

### 使用说明

运行 _music.py_ 选择你想要的 mid 文件，等待生完毕后，回车退出。
文件夹里将会多出一个 _resources.zip_ 的压缩包，_xsy_ 内的内容将会改变，将这两个文件放至 mc 地图文件夹和文件夹下 datapacks 文件夹，即可运行游戏使用

_setting.json_ 是生成程序的设置调节文件，你可以修改里面的值来决定游戏内的效果

_可能会出现选择 mid 文件但是提示说你选择的不是标准 mid 文件，这是 mido 库没办法解析，目前没办法解决_

_此外，不要选择 track0(全局音轨)内写音符信息的 mid 文件，此程序无法读取这种 mid 信息_

### 游戏内说明

要运行对应的 function，你需要两个命令方块

脉冲输入 `function xsy:(你的mid名字)/init` 运行
循环输入 `function xsy:(你的mid名字)/main` 运行

### 注意

mid 文件名一定要为英文，不得带中文或者特殊符号，否则无法运行
本文件夹内各种文件是本程序的支撑文件，请勿随意删除，修改或移动，否则导致程序无法正常运行

### _setting.json_ 说明

setting.json 格式如下

```
{
  "particleNum": 5,
  "tracks": 100,
  "effectParticle": "end_rod",
  "track1": {
    "effect": " oval end_rod star ",
    "hight": 0
  }
}
```

_"particleNum"_ 为粒子数量，0~n,推荐为 1-20 之间
_"tracks"_ 音轨的数量，可以只取 mid 文件的前几条音轨，如果大于 mid 音轨的数量，则以 mid 文件为准
_"effectParticle"_ 每个音符对应位置的粒子特效的粒子名
_"track(n)"_ 对应每条音轨的设置，effect 为路径特效，前后有空格，值之间有空格，每个值分别对应，路径效果，路径粒子名，音符特效
_"hight"_ 可以让一条音轨整体向上偏移，避免音轨过多而混乱

若 track 设置的数量小于实际的数量，多出的都以第一条设置为准

**粒子名**:以 [mcwiki](https://minecraft-zh.gamepedia.com/%E7%B2%92%E5%AD%90#.E7.B1.BB.E5.9E.8B) 上为准，若粒子名中有空格，请用 `&` 替换，如 `dust 1.0 0.5 0.5 1.0` 应该为 `dust&1.0&0.5&0.5&1.0`

**路径特效**：有

1. `straight`(直线)
1. `oval`(椭圆)
1. `brokenLine`(折线)

**音符特效**：有

1. `star`(五芒星阵)
1. `starup`(上升的五芒星)
1. `square`(立体的方块边框)

### 效果演示

[前往我的 bilibili 观看](https://space.bilibili.com/349558877)
