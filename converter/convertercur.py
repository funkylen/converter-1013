DATA = [
    {
        'type': 'RUB',
        'key': 1,
        'rate': 1,
    },
    {
        'type': 'USD',
        'key': 2,
        'rate': 60.2179,
    },
    {
        'type': 'EUR',
        'key': 3,
        'rate': 61.5416,
    },
    {
        'type': 'CNY',
        'key': 4,
        'rate': 84.4637,
    }
]


def run(option1, option2, number):
    for item in DATA:
        if item.get('key') == option1:
            rate1 = item.get('rate')
    for item in DATA:
        if item.get('key') == option2:
            rate2 = item.get('rate')
    return number * rate1 / rate2
