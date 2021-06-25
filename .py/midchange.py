import easygui as ui
import mido as md
import os
import sys
import json

# ui打开窗口，选择mid文件
while True:
    try:
        cr = ui.fileopenbox(msg="mid", title="选择midi文件",
                            default="\\*.mid", filetypes=["*.mid"], multiple=False)
        if cr == None:
            os._exit(1)
        else:
            midi_file = md.MidiFile(cr)
            fn = os.path.basename(cr).replace(".mid", "")
    except BaseException:
        result = ui.indexbox(msg='你选择的不是标准midi文件', title='错误', choices=(
            '重新选择', '退出'), image=None, default_choice='重新选择', cancel_choice='退出')
        if result == 0:
            continue
        else:
            os._exit(1)
    else:
        del cr
        break
# json文件路径
cr = os.getcwd()+"\\"+fn+".json"
kev_file = open(cr, "w", encoding="UTF-8")
# 处理写入
ppqn = int(midi_file.ticks_per_beat)
events_list = []
events_list.append(
    {'type': 'ticks_per_beat', 'value': ppqn, 'time': 0, 'is_meta': True})
tracks = 0
for i, track in enumerate(midi_file.tracks):
    name = 'track' + str(tracks)
    tracks_list = []
    for msg in track:
        msg_dict = md.Message.dict(msg)
        if msg.is_meta:
            is_metal = True
        else:
            is_metal = False
        msg_dict["is_meta"] = is_metal
        tracks_list.append(msg_dict)
    events_list.append({name: tracks_list})
    tracks += 1
kev = {'events': events_list[0], 'tracks': events_list[1:]}
r = json.dumps(kev, indent=2)
kev_file.write(r)
kev_file.close()
# 读取处理json文件
with open(fn+'.json', 'r') as fp:
    content = fp.read()
    a = json.loads(content)
ticks_per_beat = a['events']['value']
print(ticks_per_beat)
# track = a['tracks'][0]
# temponum = 0
# tempo = 0
# for i in track['track0']:
#     if i['type'] == 'set_tempo':
#         tempo += i['tempo']
#         temponum += 1
#     if i['type'] == 'time_signature':
#         numerator = i['numerator']
# tempo /= temponum
# speed = int(60000000 / tempo)
# 获取设置
with open('setting.json', 'r') as fp:
    content = fp.read()
    setting = json.loads(content)
num = 1
for i in a['tracks']:
    msg = []
    for key in i:
        print(key)
    add_time = 0
    m_add_time = 0
    for j in i[key]:
        if j['type'] == 'program_change':
            program = j['program']
        if j['type'] == 'note_on':
            m_add_time += ((add_time + j['time']) * 8 / ticks_per_beat) - \
                int((add_time + j['time']) * 8 / ticks_per_beat)
            add_time = int((add_time + j['time'])
                           * 8 / ticks_per_beat + 0.5)
            if m_add_time <= -1:
                add_time -= 1
                m_add_time += 1
            elif m_add_time > 1:
                add_time += 1
                m_add_time -= 1
            if add_time < 0:
                add_time = 0
                m_add_time -= 1
            if add_time != 0:
                msg.append('d' + str(add_time))
            msg.append(str(j['note'])+"v" +
                       str(max(round(j["velocity"]/127, 3), 0.005)))
            add_time = 0
        elif j['type'] == 'note_off':
            add_time += j['time']

    if msg != []:
        if msg[0][0] == 'd' and msg[0][1] == '0':
            msg = msg[1:]
        else:
            msg = ['0v0'] + msg
        sound = str(program+1)
        if 'sound' in setting['track'+str(num)]:
            sound = str(setting['track'+str(num)]['sound'])
        if setting['speed'] != 0:
            speed = setting['speed']
        else:
            speed = 100
        if 'track'+str(num) in setting:
            msg = [fn+setting['track'+str(num)]['effect'] + sound + ' ' + str(
                setting['track' + str(num)]['hight']) + ' ' + str(speed) + '\n'] + msg
        else:
            msg = [fn + ' oval end_rod star ' + sound +
                   ' ' + str(0) + ' ' + str(speed) + '\n'] + msg
        with open('%s%d.txt' % (fn, num), 'w') as fp:
            fp.write(' '.join(msg))
        num += 1
# 删除json
os.remove(fn+'.json')
