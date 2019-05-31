import pynput
class YGlobalScript(object):
	left_key_ = ';'
	right_key_ = '\''
	move_left_key_ = 'm'
	move_down_key_ = ','
	move_up_key_ = '.'
	move_right_key_ = '/'
	ctrl_flag_ = False
	mouse_controller_ = pynput.mouse.Controller()
	left_flag_ = False
	right_flag_ = False
	
def IsKey(key, ch):
	if key == pynput.keyboard.KeyCode.from_char(ch):
		return True
	else:
		return False

def ButtonLeft(press_flag):
	YGlobalScript.left_flag_ = press_flag
	if press_flag:
		YGlobalScript.mouse_controller_.press(pynput.mouse.Button.left)
	else:
		YGlobalScript.mouse_controller_.release(pynput.mouse.Button.left)
	return None
	
def ButtonRight(press_flag):
	YGlobalScript.right_flag_ = press_flag
	if press_flag:
		YGlobalScript.mouse_controller_.press(pynput.mouse.Button.right)
	else:
		YGlobalScript.mouse_controller_.release(pynput.mouse.Button.right)
	return None
	

def OnPress(key):
	# print('{0} press'.format(key)) #
	if (key == pynput.keyboard.Key.ctrl_l or key == pynput.keyboard.Key.ctrl_r) and not YGlobalScript.ctrl_flag_:
		YGlobalScript.ctrl_flag_ = True
	elif YGlobalScript.ctrl_flag_:
		if not YGlobalScript.left_flag_ and IsKey(key, YGlobalScript.left_key_):
			ButtonLeft(True)
		elif not YGlobalScript.right_flag_ and IsKey(key, YGlobalScript.right_key_):
			ButtonRight(True)
		elif IsKey(key, YGlobalScript.move_down_key_):
			YGlobalScript.mouse_controller_.move(0,10)
		elif IsKey(key, YGlobalScript.move_up_key_):
			YGlobalScript.mouse_controller_.move(0,-10)
		elif IsKey(key, YGlobalScript.move_left_key_):
			YGlobalScript.mouse_controller_.move(-10,0)
		elif IsKey(key, YGlobalScript.move_right_key_):
			YGlobalScript.mouse_controller_.move(10,0)

def OnRelease(key):
	print('{0} release'.format(key))
	if key == pynput.keyboard.Key.scroll_lock:
		return False
	elif key == pynput.keyboard.Key.ctrl_l or key == pynput.keyboard.Key.ctrl_r:
		YGlobalScript.ctrl_flag_ = False
		if YGlobalScript.left_flag_:
			ButtonLeft(False)
		if YGlobalScript.right_flag_:
			ButtonRight(False)
	elif YGlobalScript.ctrl_flag_:
		if IsKey(key, YGlobalScript.left_key_):
			ButtonLeft(False)
		elif IsKey(key, YGlobalScript.right_key_):
			ButtonRight(False)

with pynput.keyboard.Listener(on_press = OnPress,on_release = OnRelease) as listener:
	listener.join()
