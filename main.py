#!/usr/bin/env python3

# for windows & linux

import pynput
import time
class YGlobal(object):
    speed_up = 6
    dd = 9
    left_key_ = pynput.keyboard.Key.page_up
    right_key_ = pynput.keyboard.Key.page_down
    move_left_key_ = pynput.keyboard.Key.left
    move_down_key_ = pynput.keyboard.Key.down
    move_up_key_ = pynput.keyboard.Key.up
    move_right_key_ = pynput.keyboard.Key.right
    exit_key_ = 188 # '<'
    ctrl_flag_ = False
    mouse_controller_ = pynput.mouse.Controller()
    left_flag_ = False
    right_flag_ = False
    alt_flag_ = False

def IsKey(key, ch):
    if hasattr(key, "vk"):
        if key.vk == ch:
            return True
    else:
        if key == ch:
            return True
    return False

def ButtonLeft(press_flag):
    YGlobal.left_flag_ = press_flag
    if press_flag:
        YGlobal.mouse_controller_.press(pynput.mouse.Button.left)
    else:
        YGlobal.mouse_controller_.release(pynput.mouse.Button.left)
    return None

def ButtonRight(press_flag):
    YGlobal.right_flag_ = press_flag
    if press_flag:
        YGlobal.mouse_controller_.press(pynput.mouse.Button.right)
    else:
        YGlobal.mouse_controller_.release(pynput.mouse.Button.right)
    return None

def OnPress(key):
    time_struct = time.localtime(time.time())
    b = time.strftime('%Y %m %d %H:%M',time_struct)
    print('{1} {0} press'.format(key, b))
    if (key == pynput.keyboard.Key.alt_l or key == pynput.keyboard.Key.alt_r) \
        and not YGlobal.alt_flag_:
        YGlobal.alt_flag_ = True
    if (key == pynput.keyboard.Key.ctrl_l or key == pynput.keyboard.Key.ctrl_r) \
        and not YGlobal.ctrl_flag_:
        YGlobal.ctrl_flag_ = True
    elif YGlobal.ctrl_flag_:
        if not YGlobal.left_flag_ and IsKey(key, YGlobal.left_key_):
            ButtonLeft(True)
        elif not YGlobal.right_flag_ and IsKey(key, YGlobal.right_key_):
            ButtonRight(True)
        elif IsKey(key, YGlobal.move_down_key_):
            if YGlobal.alt_flag_:
                YGlobal.mouse_controller_.move(0,YGlobal.dd*YGlobal.speed_up)
            else:
                YGlobal.mouse_controller_.move(0,YGlobal.dd)
        elif IsKey(key, YGlobal.move_up_key_):
            if YGlobal.alt_flag_:
                YGlobal.mouse_controller_.move(0,-YGlobal.dd*YGlobal.speed_up)
            else:
                YGlobal.mouse_controller_.move(0,-YGlobal.dd)
        elif IsKey(key, YGlobal.move_left_key_):
            if YGlobal.alt_flag_:
                YGlobal.mouse_controller_.move(-YGlobal.dd*YGlobal.speed_up,0)
            else:
                YGlobal.mouse_controller_.move(-YGlobal.dd,0)
        elif IsKey(key, YGlobal.move_right_key_):
            if YGlobal.alt_flag_:
                YGlobal.mouse_controller_.move(YGlobal.dd*YGlobal.speed_up,0)
            else:
                YGlobal.mouse_controller_.move(YGlobal.dd,0)

def OnRelease(key):
    print('{0} release'.format(key)) # c++ log
    if key == pynput.keyboard.Key.alt_l or key == pynput.keyboard.Key.alt_r:
        YGlobal.alt_flag_ = False
    elif key == pynput.keyboard.Key.ctrl_l or key == pynput.keyboard.Key.ctrl_r:
        YGlobal.ctrl_flag_ = False
        if YGlobal.left_flag_:
            ButtonLeft(False)
        if YGlobal.right_flag_:
            ButtonRight(False)
    elif YGlobal.ctrl_flag_:
        if IsKey(key, YGlobal.left_key_):
            ButtonLeft(False)
        elif IsKey(key, YGlobal.right_key_):
            ButtonRight(False)
        elif IsKey(key, YGlobal.exit_key_):
            return False

print("""**使用说明**
键盘组合键    等价于鼠标的操作
Ctrl + '←'      鼠标向左移动
Ctrl + '↓'      鼠标向下移动
Ctrl + '↑'      鼠标向上移动
Ctrl + '→'      鼠标向右移动
Ctrl + pageup   按下鼠标左键
Ctrl + pagedown 按下鼠标右键
Ctrl + '<'      终止程序
(Alt键可以6倍速移动)""")

with pynput.keyboard.Listener(on_press = OnPress,on_release = OnRelease) as listener:
    listener.join()
