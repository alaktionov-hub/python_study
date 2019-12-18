#!/usr/bin/env python3
class MyFerum:
    temp_pl = 1538
    temp_isp = 2862

    def condition(self, temp):
        if temp < self.temp_pl:
            print("solid")
        elif temp > self.temp_isp and temp < self.temp_pl:
            print("liguid")
        else:
            print("vapor")


run = MyFerum()
run.condition(666)
