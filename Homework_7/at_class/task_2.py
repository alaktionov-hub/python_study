#!/usr/bin/env python3

# sizes = {'S': {'ru': 40, 'eu': 34, 'fr': 38, 'it': 38, 'gb': 8, 'usa': 6},
#         'M': {'ru': 42-44, 'eu': 36-38, 'fr': 38-40, 'it': 40-42, 'gb': 10-12, 'usa': 8-10},
#         'L': {'ru': 46-48, 'eu': 40-42, 'fr': 42-44, 'it': 44-46, 'gb': 14-16, 'usa': 12-14},
#         'XL': {'ru': 50-52, 'eu': 44-46, 'fr': 46-48, 'it': 48-50, 'gb': 18-20, 'usa': 16-18},
#         'XXL': {'ru': 54, 'eu': 48, 'fr': 50, 'it': 52, 'gb': 22, 'usa': 20}}

sizes = sizes_international = {'S': {'ru': '40', 'eu': '34', 'fr': '38', 'it': '38', 'gb': '8', 'usa': '6'},
                               'M': {'ru': '42-44', 'eu': '36-38', 'fr': '38-40', 'it': '40-42', 'gb': '10-12', 'usa': '8-10'},
                               'L': {'ru': '46-48', 'eu': '40-42', 'fr': '42-44', 'it': '44-46', 'gb': '14-16', 'usa': '12-14'},
                               'XL': {'ru': '50-52', 'eu': '44-46', 'fr': '46-48', 'it': '48-50', 'gb': '18-20', 'usa': '16-18'},
                               'XXL': {'ru': '54', 'eu': '48', 'fr': '50', 'it': '52', 'gb': '22', 'usa': '20'}}

sizes_ru = {'40': {'international': 'S', 'eu': '34', 'fr': '38', 'it': '38', 'gb': '8', 'usa': '6'},
            '42': {'international': 'M', 'eu': '36-38', 'fr': '38-40', 'it': '40-42', 'gb': '10-12', 'usa': '8-10'},
            '44': {'international': 'M', 'eu': '36-38', 'fr': '38-40', 'it': '40-42', 'gb': '10-12', 'usa': '8-10'},
            '46': {'international': 'L', 'eu': '40-42', 'fr': '42-44', 'it': '44-46', 'gb': '14-16', 'usa': '12-14'},
            '48': {'international': 'L', 'eu': '40-42', 'fr': '42-44', 'it': '44-46', 'gb': '14-16', 'usa': '12-14'},
            '50': {'international': 'XL', 'eu': '44-46', 'fr': '46-48', 'it': '48-50', 'gb': '18-20', 'usa': '16-18'},
            '52': {'international': 'XL', 'eu': '44-46', 'fr': '46-48', 'it': '48-50', 'gb': '18-20', 'usa': '16-18'},
            '54': {'international': 'XXL', 'eu': '48', 'fr': '50', 'it': '52', 'gb': '22', 'usa': '20'}}


# def find_size(size):
#    return print(sizes_international[size])


# print(sizes['S'])
# find_size('S')
#print("What you can choose: " + "international , RU")


size_type = input("Enter type (ru / international)")

size = input("Enter size: ")

to_out = input("What type of you want to get: ")


def find_size(size_type_f, size_f, to_out_f):
    return size[size_type][sizes][to_out]
