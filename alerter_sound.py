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
        #self.alexa("ガスコンロの温度が上がりました")
        self.alexa("点火しました")
        log.info("Got HOT")

    def go_cold(self):
        print("==> Be COLD")
        playsound("sound/GoCold.mp3")
        #self.alexa("ガスコンロの温度が下がりました")
        self.alexa("火が消えました")
        log.info("Got COLD")

    def hot_alarm(self, duration, temp):
        print("==> HOT ALARM:", duration, "sec")
        playsound("sound/HotAlarm.mp3")
        self.alexa("温度が高い状態で{}分、たちました。温度は{}度です。".format(int(duration / 60), int(temp)))
        log.info("Alarm HOT")
