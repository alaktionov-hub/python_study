#!/usr/bin/env python3


class Element:
    def __init__(self, t_isp, t_pl):
        self.t_isp = t_isp
        self.t_pl = t_pl

    def condition(self, temp, gr):
        if gr == 'K' or gr == 'k':
            t = temp - 273
        elif gr == 'C' or gr == 'c':
            t = temp
        else:
            print('Unknown system!')
            return
        if t < self.t_pl:
            print('solid')
        elif t > self.t_pl-1 and t < self.t_isp:
            print('liquid')
        else:
            print('vapor')

    def convertor_to_c(self, temp, gr):
        if gr not in ['K', 'F', 'C']:
            raise ValueError
        result = temp
        if gr == 'K':
            result = temp + 273
        elif gr == 'F':
            result = temp*9/5 + 32
        return result


class Iron(Element):
    t_pl = 1538
    t_isp = 2862


#iron = Iron()
iron = Element(1555, 3333)
#print(iron.convertor_to_c(400, 'C'))
iron.condition(3000, 'C')
