# For modules
import json
from datetime import datetime
from psutil import disk_usage, sensors_battery
from psutil._common import bytes2human
from socket import gethostname, gethostbyname
from subprocess import check_output

class Block():
    def __init__(self, name, full_text_command = None, short_text_command=None, color=None,
            background=None, border=None, min_width=None, align="center", urgent=None,
            instance=None, separator=True, separator_block_width=15, others=[]):
        self.data = {}
        self.data["full_text"] = None
        self.data["name"] = name
        self.data["instance"] = instance 
        self.data["color"] = color
        self.data["background"] = background
        self.data["separator"] = separator
        self.data["separator_block_width"] = separator_block_width
        self.data["border"] = border
        self.data["min_width"] = min_width
        self.data["align"] = align
        self.data["urgent"] = urgent
        self.data["_others"] = others

        self.full_text_command = full_text_command
        self.short_text_command = short_text_command 
    
    def gen_text(self):
        if self.full_text_command is not None:
            try:
                self.data["full_text"] = check_output(self.full_text_command, shell=True).strip().decode("utf-8")
            except Exception:
                self.data["full_text"] = None
        if self.short_text_command is not None:
            try:
                self.data["short_text"] = check_output(self.short_text_command, shell=True).strip().decode("utf-8")
            except Exception:
                self.data["short_text"] = None

        return json.dumps(self.data)


class Battery(Block):

    def gen_text(self):
        if sensors_battery().power_plugged:
            status = "Charging: "
            status_short = "(C)"
        else:
            status = "Discharging: "
            status_short = "(D)"
        percentage = int(sensors_battery().percent)

        if percentage <= 20:
            self.data["color"] = "#ff0000"
        elif percentage <= 50 and percentage > 20:
            self.data["color"] = "#ffff00"
        elif percentage <= 75 and percentage > 50:
            self.data["color"] = "#ff8800"
        else:
            self.data["color"] = "#00FF00"

        self.data["full_text"] = status + str(percentage) + "%"
        self.data["short_text"] = status_short + str(percentage) + "%"

        return json.dumps(self.data)


class Disk(Block):
    def gen_text(self):
        if self.data["instance"] == None:
            self.data["full_text"] = None
        else:
            self.data["full_text"] = self.data["instance"] + ": " + bytes2human(disk_usage(self.data["instance"]).free)

        return json.dumps(self.data)


class Brightness(Block):
    def gen_text(self):
        self.data["full_text"] = "Brightness: " + str(round(float(check_output("light -G", shell=True).strip().decode("utf-8")))) + "%"
        self.data["short_text"] = "SB: " + str(round(float(check_output("light -G", shell=True).strip().decode("utf-8")))) + "%"

        return json.dumps(self.data)