# делаем что-то со строкой
def strings_fun():
    str_1 = str('sample')
    str_2 = str()

    for i in range(0, len(str_1)):
        str_2 += str_1[i:] + str_1[:i] + '\n'

    print(str_2)


# заносим кортеж в словарь, записывая тип данных
def dicts_fun(t):
    if not isinstance(t, tuple):
        print('t не является кортежем')
        return

    my_dict = dict()

    for i in range(0, len(t)):
        my_dict[t[i]] = type(t[i]).__name__

    print('Типы данных в кортеже:')
    for i in my_dict:
        print('{0:<10} {1:>5}'.format(i, my_dict.get(i)))
    print()


# находим числа в кортеже и вычисляем их сумму
def tuple_elements_sum(t):
    sum = int()

    for i in t:
        if isinstance(i, int):
            sum += i

    print('Сумма чисел в кортеже:', sum, '\n')


# пользовательский кортеж
def own_tuple():
    n = int(input('Введите число элементов кортежа: '))

    my_tuple = tuple()

    for i in range(0, n):
        value = input('{0}. '.format(i+1))

        try:
            my_tuple = my_tuple + (int(value),)
        except ValueError:
            my_tuple = my_tuple + (value, )

    tuple_elements_sum(my_tuple)
    dicts_fun(my_tuple)


if __name__ == '__main__':
    strings_fun()

    t = 'abc', 1234, 'text', 6782
    tuple_elements_sum(t)
    dicts_fun(t)

    if input('Ввести свой кортеж? y/n: ') == 'y':
        own_tuple()
    else:
        print('Как хотите...')
