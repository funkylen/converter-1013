import prompt


def input_key(key):
    while True:
        firstkey = prompt.string("Выберите единицу: ")
        if firstkey in key:
            break
    return firstkey


def get_factor(unit_for_chek, key_table):
    for key in key_table:
        if unit_for_chek == key['единица измерения']:
            return key['множитель']


def convert():
    keys_table = [{'единица измерения': 'm', 'множитель': 1},
                   {'единица измерения': 'mm', 'множитель': 0.001},
                   {'единица измерения': 'cm', 'множитель': 0.01},
                   {'единица измерения': 'km', 'множитель': 1000},
                   {'единица измерения': 'nm', 'множитель': 0.000000001}
                   ]
    keys = [key['единица измерения'] for key in keys_table]
    user_num = prompt.real("Введите число: ")
    for key in keys_table:
        print(key['единица измерения'])

    firstkey = input_key(key)
    secondkey = input_key(keys)

    firsted = get_ed(firstkey, keys_table)
    seconded = get_ed(secondkey, keys_table)

    result = float(user_num) * firsted / seconded
    print(result)