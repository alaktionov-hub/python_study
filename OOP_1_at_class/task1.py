#!/usr/bin/env python3


class Ferum:
    t_pl = 1538
    t_isp = 2862

    def condition(self, temp, gr):
        if gr == 'K' or gr == 'k':
            if temp < self.t_pl+273:
                print('solid')
            elif temp > self.t_pl+272 and temp < self.t_isp+273:
                print('liquid')
            else:
                print('vapor')
        elif gr == 'C' or gr == 'c':
            if temp < self.t_pl:
                print('solid')
            elif temp > self.t_pl-1 and temp < self.t_isp:
                print('liquid')
            else:
                print('vapor')
        else:
            print('Unknown system!')


fe = Ferum()
fe.condition(35)
