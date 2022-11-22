import prompt


def input_unit(units):
    while True:
        firstunit = prompt.string("Выберите единицу: ")
        if firstunit in units:
            break
    return firstunit


def get_factor(unit_for_chek, units_table):
    for unit in units_table:
        if unit_for_chek == unit['единица измерения']:
            return unit['множитель']


def convert():
    units_table = [{'единица измерения': 'm', 'множитель': 1},
                   {'единица измерения': 'mm', 'множитель': 0.001},
                   {'единица измерения': 'cm', 'множитель': 0.01},
                   {'единица измерения': 'km', 'множитель': 1000},
                   {'единица измерения': 'nm', 'множитель': 0.000000001}
                   ]
    units = [unit['единица измерения'] for unit in units_table]
    user_num = prompt.real("Введите число: ")
    for unit in units_table:
        print(unit['единица измерения'])

    firstunit = input_unit(units)
    secondunit = input_unit(units)

    firstfactor = get_factor(firstunit, units_table)
    secondfactor = get_factor(secondunit, units_table)

    result = float(user_num) * firstfactor / secondfactor
    print(result)