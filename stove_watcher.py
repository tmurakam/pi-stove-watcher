# Stove watcher

import time

HOT_THRESHOLD = 60.0
ALARM_INTERVAL = 60 * 5


class StoveWatcher:
    is_hot = False
    last_alarm = 0
    last_hot_trigger = 0

    def __init__(self, alerter):
        self.alerter = alerter

    def watch(self, temps):
        now = time.time()
        max_temp = max(temps)
        print("Temp =", max_temp)

        if max_temp >= HOT_THRESHOLD:
            if not self.is_hot:
                # Go hot
                self.is_hot = True
                self.last_alarm = now
                self.last_hot_trigger = now
                self.alerter.go_hot()

            else:
                if now - self.last_alarm >= ALARM_INTERVAL:
                    self.alerter.hot_alarm(now - self.last_hot_trigger)
                    self.last_alarm = now

        else:
            if self.is_hot:
                self.is_hot = False
                self.alerter.go_cold()
