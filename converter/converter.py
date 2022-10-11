import prompt

CM_IN_M = 100
M_IN_KM = 1000


def print_menu(modes):
    print('Выбор типа конвертации')

    for mode in modes:
        index = mode.get('index')

        from_type = mode.get('from_type')
        to_type = mode.get('to_type')

        print(f'{index}. {from_type} -> {to_type}')


def get_modes():
    return [
        {
            'index': 1,
            'from_type': 'CM',
            'to_type': 'M',
            'handler': lambda centimeters: centimeters / CM_IN_M,
        },
        {
            'index': 2,
            'from_type': 'M',
            'to_type': 'CM',
            'handler': lambda meters: meters * CM_IN_M,
        },
        {
            'index': 3,
            'from_type': 'M',
            'to_type': 'KM',
            'handler': lambda meters: meters / M_IN_KM,
        },
    ]


def convert():
    modes = get_modes()

    print_menu(modes)

    convert_type = prompt.integer('Выберите тип: ')

    number = prompt.real('Введите значение: ')

    for mode in modes:
        if convert_type == mode.get('index'):
            converted_number = mode.get('handler')(number)

            from_type = mode.get('from_type')
            to_type = mode.get('to_type')

            print(f'{number} {from_type} -> {converted_number} {to_type}')
            return

    raise 'Неизвестный тип конвертации'
