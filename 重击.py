import keyboard
import threading
import time
import mouse

stop_flag = True
running_flag = False


def simulate_keys_and_mouse():
    global stop_flag, running_flag
    running_flag = True
    while not stop_flag:
        keyboard.press('.')
        time.sleep(0.02)
        keyboard.release('.')
        time.sleep(1)  # 可根据需要调整间隔

    running_flag = False


def start_program():
    global stop_flag
    if not running_flag:
        print("程序开始")
        stop_flag = False
        threading.Thread(target=simulate_keys_and_mouse).start()


def stop_program(e):
    global stop_flag
    if e.event_type == keyboard.KEY_DOWN and e.name == '=':
        print("程序终止")
        stop_flag = True


keyboard.add_hotkey('-', start_program)
keyboard.on_press_key('=', stop_program)

keyboard.wait('esc')
