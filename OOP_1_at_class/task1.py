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

    def convert(self, temp, gr):
        if gr not in ['F', 'C', 'K']:
            raise ValueError
        result = temp
        if gr == 'K':
            result = temp+273
        elif gr == 'F':
            result = temp*9/5+32
        return result


fe = Ferum()
fe.condition(20000, 'K')
fe.condition(15, 'C')
fe.condition(1699, 'C')


print(fe.convert(200, 'F'))
print(fe.convert(33, 'C'))
print(fe.convert(12, 'K'))
