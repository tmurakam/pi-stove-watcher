# Alerter

import os
from logging import getLogger

from playsound import playsound

DEVICE = "Living Echo"

log = getLogger(__name__)


class Alerter:
    def alexa(self, text):
        os.system("./alexa_remote_control.sh -d '{}' -e 'speak:{}'".format(DEVICE, text))

    def startup(self):
        print("==> Started")
        playsound("sound/GoHot.mp3")
        self.alexa("ガスコンロの監視を開始しました")
        log.info("Start watching")

    def go_hot(self):
        print("==> Got HOT")
        playsound("sound/GoHot.mp3")
        self.alexa("ガスコンロの温度が上がりました")
        log.info("Got HOT")

    def go_cold(self):
        print("==> Be COLD")
        playsound("sound/GoCold.mp3")
        self.alexa("ガスコンロの温度が下がりました")
        log.info("Got COLD")

    def hot_alarm(self, duration):
        print("==> HOT ALARM:", duration, "sec")
        playsound("sound/HotAlarm.mp3")
        self.alexa("ガスコンロの温度が上がったままです")
        log.info("Alarm HOT")
