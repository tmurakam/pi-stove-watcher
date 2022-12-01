# Alerter

from playsound import playsound

class Alerter:
    def go_hot(self):
        print("==> Go HOT")
        playsound("sound/GoHot.mp3")

    def go_cold(self):
        print("==> Go COLD")
        playsound("sound/GoCold.mp3")

    def hot_alarm(self, duration):
        print("==> HOT ALARM:", duration, "sec")
        playsound("sound/HotAlarm.mp3")
