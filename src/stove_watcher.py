# Stove watcher

import time

THR_H = 90.0
THR_L = 70.0

ALARM_INTERVAL = 60 * 5


class StoveWatcher:
    is_hot = False
    last_alarm = 0
    last_hot_trigger = 0

    def __init__(self, alerter):
        self.alerter = alerter

    def watch(self, temps):
        max_temp = max(temps)

        now = time.time()
        if self.is_hot:
            hot_duration = now - self.last_hot_trigger
            print("[H] Temp =", max_temp, "Hot duration =", hot_duration)
        else:
            print("[C] Temp =", max_temp)

        if max_temp >= THR_H and not self.is_hot:
            # Enter hot state
            self.is_hot = True
            self.last_alarm = now
            self.last_hot_trigger = now
            self.alerter.go_hot()

        elif max_temp <= THR_L and self.is_hot:
            # Enter cold state
            self.is_hot = False
            self.alerter.go_cold()

        if self.is_hot and now - self.last_alarm >= ALARM_INTERVAL:
            self.alerter.hot_alarm(now - self.last_hot_trigger, max_temp)
            self.last_alarm = now

        return max_temp
