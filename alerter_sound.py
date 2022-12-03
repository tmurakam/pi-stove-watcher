# Alerter

import os

from playsound import playsound

DEVICE = "Living Echo"


class Alerter:
    def alexa(self, text):
        os.system("./alexa_remote_control.sh -d '{}' -e 'speak:{}'".format(DEVICE, text))

    def startup(self):
        print("==> Started")
        playsound("sound/GoHot.mp3")
        self.alexa("ガスコンロの監視を開始しました")

    def go_hot(self):
        print("==> Go HOT")
        playsound("sound/GoHot.mp3")
        self.alexa("ガスコンロの温度が上がりました")

    def go_cold(self):
        print("==> Go COLD")
        playsound("sound/GoCold.mp3")
        self.alexa("ガスコンロの温度が下がりました")

    def hot_alarm(self, duration):
        print("==> HOT ALARM:", duration, "sec")
        playsound("sound/HotAlarm.mp3")
        self.alexa("ガスコンロの温度が上がったままです")
