import time
import os

def loading():
    animation = [
    "--------- LOADING [        ] ---------",
    "--------- LOADING [=       ] ---------",
    "--------- LOADING [===     ] ---------",
    "--------- LOADING [====    ] ---------",
    "--------- LOADING [=====   ] ---------",
    "--------- LOADING [======  ] ---------",
    "--------- LOADING [======= ] ---------",
    "--------- LOADING [========] ---------",
    "--------- LOADING [ =======] ---------",
    "--------- LOADING [  ======] ---------",
    "--------- LOADING [   =====] ---------",
    "--------- LOADING [    ====] ---------",
    "--------- LOADING [     ===] ---------",
    "--------- LOADING [      ==] ---------",
    "--------- LOADING [       =] ---------",
    "--------- LOADING [        ] ---------",
    "--------- LOADING [        ] ---------" ]
    notcomplete = True
    i = 0
    while notcomplete:
        print(animation[i % len(animation)], end='\r')
        time.sleep(.1)
        i += 1
        if i == 30:
            print('\n')
            break


folder_start = 'Z_BMOframes_Start'

def animatedbmo_start(nama_folder, repeat = 1):
    filenames = []
    for i in range(23):
        filenames.append(f"{nama_folder}/{i}.txt")

    frames = []
    for name in filenames:
        with open(name, "r", encoding="utf8") as f:
            frames.append(f.readlines())

    for i in range(repeat):
        for frame in frames:
            print("".join(frame))
            time.sleep(0.083)

    print('''
======================================================================================

▒█▀▀▀█ ▒█▀▀▀ ▒█░░░ ░█▀▀█ ▒█▀▄▀█ ░█▀▀█ ▀▀█▀▀ 　 ▒█▀▀▄ ░█▀▀█ ▀▀█▀▀ ░█▀▀█ ▒█▄░▒█ ▒█▀▀█ 
░▀▀▀▄▄ ▒█▀▀▀ ▒█░░░ ▒█▄▄█ ▒█▒█▒█ ▒█▄▄█ ░▒█░░ 　 ▒█░▒█ ▒█▄▄█ ░▒█░░ ▒█▄▄█ ▒█▒█▒█ ▒█░▄▄ 
▒█▄▄▄█ ▒█▄▄▄ ▒█▄▄█ ▒█░▒█ ▒█░░▒█ ▒█░▒█ ░▒█░░ 　 ▒█▄▄▀ ▒█░▒█ ░▒█░░ ▒█░▒█ ▒█░░▀█ ▒█▄▄█

======================================================================================

    ''')
# control
#animatedbmo_start(folder_start)

folder_end = 'Z_BMOframes_End'
def animatedbmo_end(nama_folder, repeat = 2):
    filenames = []
    for i in range(14):
        filenames.append(f"{nama_folder}/{i}.txt")

    frames = []
    for name in filenames:
        with open(name, "r", encoding="utf8") as f:
            frames.append(f.readlines())

    for i in range(repeat):
        for frame in frames:
            print("".join(frame))
            time.sleep(0.083)

    print('''
======================================================================================

                            █▀▀▄ █░░█ █▀▀ 　 █▀▀▄ █░░█ █▀▀ 　 ▄ ▄▀ 
                            █▀▀▄ █▄▄█ █▀▀ 　 █▀▀▄ █▄▄█ █▀▀ 　 ░ █░ 
                            ▀▀▀░ ▄▄▄█ ▀▀▀ 　 ▀▀▀░ ▄▄▄█ ▀▀▀ 　 ▀ ▀▄

======================================================================================

    ''')

animatedbmo_end("../data/Z_BMOframes_End")