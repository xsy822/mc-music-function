# mc-music-function

**根据指定格式文本乐谱生成 mc 粒子音乐 function 包**

---

### 声明

本程序只用于个人实验，参观欣赏。若用于公开影像交流，文章等，须先告知作者，并在作品下注明引用来源。
联系方式：
[bilibili](https://space.bilibili.com/349558877)
[博客留言](https://blog.xiaoshiyan.top)
[邮箱](mailto:2239499647@qq.com)

### 使用说明

运行 _music.py_ 选择你想要的 mid 文件，等待生完毕后，回车退出。
文件夹里将会多出一个 _resources.zip_ 的压缩包，_xsy_ 内的内容将会改变，将这两个文件放至 mc 地图文件夹和文件夹下 datapacks 文件夹，即可运行游戏使用

_setting.json_ 是生成程序的设置调节文件，你可以修改里面的值来决定游戏内的效果

_可能会出现选择 mid 文件但是提示说你选择的不是标准 mid 文件，这是 mido 库没办法解析，目前没办法解决_

_此外，不要选择 track0(全局音轨)内写音符信息的 mid 文件，此程序无法读取这种 mid 信息_

### 游戏内说明

要运行对应的 function，你需要两个命令方块

- 脉冲输入 `function xsy:(你的mid名字)/init` 运行
- 循环输入 `function xsy:(你的mid名字)/main` 运行

### 注意

mid 文件名一定要为英文，不得带中文或者特殊符号，否则无法运行
本文件夹内各种文件是本程序的支撑文件，请勿随意删除，修改或移动，否则导致程序无法正常运行

### _setting.json_ 说明

setting.json 格式如下

```
{
  "url": "D:\\MCLDownload\\Game\\.minecraft\\saves\\MCGame-af98a4c4-73ea-4c35-82fb-001ecca32948\\",
  "particleNum": 5,
  "tracks": 100,
  "speed":100,
  "effectParticle": "end_rod",
  "track1": {
    "effect": " oval end_rod star ",
    "hight": 0,
    "sound"：0,
  }
}
```

- _"url"_ 为 mc 地图对应的地址（自动部署，不过注意不要在游戏运行时操作，正在使用的文件无法删除），斜杠应输两个（转义），最后需要加上两个斜杠，若值为空则不移动，需要手动移动
- _"particleNum"_ 为粒子数量，0~n,推荐为 1-20 之间
- _"tracks"_ 音轨的数量，可以只取 mid 文件的前几条音轨，如果大于 mid 音轨的数量，则以 mid 文件为准
- _"speed"_ 速度（bpm）,须手动设置
- _"effectParticle"_ 每个音符对应位置的粒子特效的粒子名
- _"track(n)"_ 对应每条音轨的设置，effect 为路径特效，前后有空格，值之间有空格，每个值分别对应，路径效果，路径粒子名，音符特效
  - _"hight"_ 可以让一条音轨整体向上偏移，避免音轨过多而混乱
  - _"sound"_ 可选填，该值为指定音色，为 0 则是打击乐，其他参照标准 mid 音色表

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
