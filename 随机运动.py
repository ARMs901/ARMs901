import random
import time
import threading
import keyboard

# 全局变量
running = False
exit_flag = False

# 随机生成按键和时长的函数
def random_key_and_duration():
    keys = ['w', 'a', 's', 'd']
    key = random.choice(keys)
    duration = random.uniform(0.3, 0.9)  # 随机生成按键时长
    return key, duration

# 线程函数，用于随机输出按键
def random_key_thread():
    global running, exit_flag
    while not exit_flag:
        if running:
            '''key, duration = random_key_and_duration()
            print(f"Key: {key}, Duration: {duration:.2f} seconds")
            time.sleep(duration)'''
            key, duration = random_key_and_duration()
            keyboard.press(key)
            time.sleep(duration)
            keyboard.release(key)
            keyboard.press(',')
            time.sleep(0.6)
            keyboard.release(',') # 为避免连续按键过快，增加一点延时-


# 主程序
def main():
    global running, exit_flag

    print("Press '-' to start and '=' to exit.")

    random_thread = threading.Thread(target=random_key_thread)
    random_thread.start()

    while not exit_flag:
        if keyboard.is_pressed('-'):  # 使用 keyboard 模块检测按键
            running = True
        elif keyboard.is_pressed('='):
            running = False

    exit_flag = True
    random_thread.join()

if __name__ == "__main__":
    main()
