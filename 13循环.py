import keyboard
import threading
import time

stop_flag = True
running_flag = False

def simulate_keys():
    global stop_flag, running_flag
    running_flag = True
    while not stop_flag:
        for _ in range(68):
            keyboard.press('1')
            keyboard.release('1')
            time.sleep(0.1)  # 小间隔
        keyboard.press('3')
        keyboard.release('3')
        time.sleep(0.2)  # 小间隔
    running_flag = False

def start_program():
    global stop_flag
    if not running_flag:
        print("程序开始")
        stop_flag = False
        threading.Thread(target=simulate_keys).start()

def stop_program(e):
    global stop_flag
    if e.event_type == keyboard.KEY_DOWN and e.name == '=':
        print("程序终止")
        stop_flag = True

keyboard.add_hotkey('-', start_program)
keyboard.on_press_key('=', stop_program)

keyboard.wait('esc')
