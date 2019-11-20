def spam(number):
    '''Function should return something like this:
    spam(1);#bulochka
    spam(3);#bulochkabulochkabulochka
    But it is broken. Fix it please!

    Эта функция принимает числовой параметр. Должна вернуть строку, которая
    повторяется столько раз, сколько параметров передано. Она уже написана,
    но не работает. Любым способом заставьте ее работать.
    '''
#    return ['bulochka' for i in range(number+1)]

    return ("bulochka"*number)  # just * to number


def my_sum(list_of_numbers):
    """Function receives a list with integer numbers,
    should return its sum as an integer. Do not use built in summarize functions.
    :param list

    Функция получает на вход массив чисел, должна вернуть сумму этих чисел.
    Не использовать встроенные функции суммирования.

    """
    element = 0
    for number in list_of_numbers:
        element += number  # sum all
    return element

    pass


def shortener(string):
    """
    Function receives a long string with many words.
    It should return the same string, but words,
    larger then 6 symbols should be changed, symbols
    after the sixth one should be replaced by symbol *
    :param string
    :returns string

     Функция получает на вход длинную строку с множеством слов.
     Она должна вернуть ту же строку, но в словах, которые длиннее 6 символов,
     функция должна вместо всех символов после шестого поставить одну звездочку.
     Пример: Из слова 'verwijdering' должно получиться 'verwij*'


        """
    # for word in list:

    input_list = string.split(" ")  # split by word
    out_list = []  # new list with chnaged
    for word in input_list:  # check if more than 6
        if len(word) > 6:  # check if world have ,ore that 6
            out_list.append(word[0:6]+"*")  # chnage and append with *
        else: 
            out_list.append(word)  # on other case just add word back
    return (" ").join(out_list)  # retur new list

    pass
    #  ...wite your code here


def compare_ends(words):
    """
    Function receives an array of strings.
    Please return number of strings, which
    length is at least 2 symbols and first character
    is equal to the last character

    Функция получает на вход массив строк. Вернуть надо количество строк,
    которые не короче двух символов и у которых первый и последний
    символ совпадают.

    """
#    my_list = []  # our new list
    count = 0  #
    for word in words:
        # if len(word) > 2 and word[0] == word[-1]:
        if len(word) > 1 and word[0] == word[-1]:
            count += 1
            print(word)
    return count
    pass
    #  ...wite your code here
