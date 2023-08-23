import random
import time
import threading
from pynput import keyboard

# 全局变量
running = False
exit_flag = False
controller = keyboard.Controller()

# 随机生成按键和时长的函数
def random_key_and_duration():
    keys = ['w', 's', 'a', 'd', ',']
    key = random.choice(keys)
    duration = random.uniform(0.4, 0.9)  # 随机生成按键时长
    return key, duration

# 线程函数，用于自动按下和松开按键
def auto_key_thread():
    global running, exit_flag, controller
    while not exit_flag:
        if running:
            key, duration = random_key_and_duration()
            with controller.pressed(key):
                time.sleep(duration)
            time.sleep(0.01)  # 为避免连续按键过快，增加一点延时

# 主程序
def main():
    global running, exit_flag

    print("Press '-' to start and '=' to exit.")

    auto_thread = threading.Thread(target=auto_key_thread)
    auto_thread.start()

    def on_key_release(key):
        global running, exit_flag
        try:
            if key.char == '-':
                running = True
            elif key.char == '=':
                running = False
        except AttributeError:
            pass

    listener = keyboard.Listener(on_release=on_key_release)
    listener.start()

    while not exit_flag:
        time.sleep(0.1)

    exit_flag = True
    auto_thread.join()

if __name__ == "__main__":
    main()
