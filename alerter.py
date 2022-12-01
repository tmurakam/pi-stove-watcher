# Alerter
class Alerter:
    def go_hot(self):
        print("==> Go HOT")

    def go_cold(self):
        print("==> Go COLD")

    def hot_alarm(self, duration):
        print("==> HOT ALARM:", duration, "sec")
