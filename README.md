# mc-music-function

**根据指定格式文本乐谱生成 mc 粒子音乐 function 包**

---

## music.py

Track 类创建一个新的工程

- funName(参数): 函数名(默认'test')

* add(方法): 增加一个音符
  - tone: 音调，降 1 开始的递增数(1,2,3...)
  - delay: 上一音符与下一音符的间隔时间(单位是 1/16 拍)
  - effect: 每个音符对应位置粒子特效(默认是五角星，effect.star)

### effect.py

star 函数：指定坐标生成一个五角星

- particle: 粒子名称(mc 粒子名称)
- pos: 三维坐标([x,y,z]，mc 标准)
- r: 五角星外接圆半径
- fp: 文件指针(写入位置)
