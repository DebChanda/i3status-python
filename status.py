#! /usr/bin/env python3


import json
import argparse
from types import MethodType
from time import sleep

# Import modules

from modules import Block, Battery, Disk, Brightness


ssid = Block("ssid", "iwgetid -r", color="#ffff00")
show_time = Block("date", "date +'%I:%M %p'")
battery = Battery("battery")
brightness = Brightness("brightness")
disk_home = Disk('disk', instance="/home")

blocks = [brightness, battery, disk_home, ssid, show_time]

def refresh():
    # disk = bytes2human(disk_usage('/').free)
    # ip = gethostbyname(gethostname())

    # date = datetime.now().strftime('%h %d %A %I:%M %p')
    print("[")
    for block in blocks:
        print(block.gen_text())
        print(",")
    print("],")


def start():
    # stdout.flush()
    header = json.dumps({ "version": 1, "click_events": True})
    print(header + "\n" + "[\n[],")

if __name__ == "__main__":
    start()
    while True:
        refresh()
        sleep(5)

