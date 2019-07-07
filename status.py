#! /usr/bin/env python3


import json
import argparse
from types import MethodType
from time import sleep

# Import modules

from modules import Block, Battery

# class BLOCK():
#     def __init__(self, name, full_text_command = None, short_text_command=None, color=None,
#             background=None, border=None, min_width=None, align="center", urgent=None,
#             instance=None, separator=True, separator_block_width=15, others=[]):
#         self.data = {}
#         self.data["full_text"] = None
#         self.data["name"] = name
#         self.data["instance"] = instance 
#         self.data["color"] = color
#         self.data["background"] = background
#         self.data["separator"] = separator
#         self.data["separator_block_width"] = separator_block_width
#         self.data["border"] = border
#         self.data["min_width"] = min_width
#         self.data["align"] = align
#         self.data["urgent"] = urgent
#         self.data["_others"] = others

#         self.full_text_command = full_text_command
#         self.short_text_command = short_text_command 
    
#     def gen_text(self):
#         if self.full_text_command is not None:
#             try:
#                 self.data["full_text"] = check_output(self.full_text_command, shell=True).strip().decode("utf-8")
#             except Exception:
#                 self.data["full_text"] = None
#         if self.short_text_command is not None:
#             try:
#                 self.data["short_text"] = check_output(self.short_text_command, shell=True).strip().decode("utf-8")
#             except Exception:
#                 self.data["short_text"] = None

#         return json.dumps(self.data)

ssid = Block("ssid", "iwgetid -r", color="#ffff00")
show_time = Block("date", "date +'%I:%M %p'")
battery = Battery("battery")

# def battery_gen_text(self):
#     if sensors_battery().power_plugged:
#         status = "Charging: "
#         status_short = "(C)"
#     else:
#         status = "Discharging: "
#         status_short = "(D)"
#     percentage = int(sensors_battery().percent)

#     if percentage <= 20:
#         self.data["color"] = "#ff0000"
#     elif percentage <= 50 and percentage > 20:
#         self.data["color"] = "#ffff00"
#     elif percentage <= 75 and percentage > 50:
#         self.data["color"] = "#ff8800"
#     else:
#         self.data["color"] = "#00FF00"

#     self.data["full_text"] = status + str(percentage) + "%"
#     self.data["short_text"] = status_short + str(percentage) + "%"

#     return json.dumps(self.data)

# battery.gen_text = MethodType(battery_gen_text, battery)

blocks = [battery, ssid, show_time]

def refresh():
    # disk = bytes2human(disk_usage('/').free)
    # ip = gethostbyname(gethostname())
    # try:
    #     ssid = check_output("iwgetid -r", shell=True).strip().decode("utf-8")
    #     ssid = "(%s)" % ssid
    # except Exception:
    #     ssid = "None"
    # battery = int(sensors_battery().percent)
    # status = "Charging" if sensors_battery().power_plugged else "Discharging"
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
        sleep(2)

