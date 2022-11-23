import prompt
from converter.convertercur import run, DATA


def input_option(message, array):
    option = prompt.integer(message)

    while option not in array:
        option = prompt.integer(message)
    return option


def user_input():
    message = "Выберите:\n"
    for item in DATA:
        type = item.get('type')
        key = item.get('key')

        message += f"{key}. {type}\n"

    array = [item.get('key') for item in DATA]

    option1 = input_option(message, array)

    message = "Выберите :\n"
    for item in DATA:
        type = item.get('type')
        key = item.get('key')

        message += f"{key}. {type}\n"

    option2 = input_option(message, array)

    number = prompt.real("Введите число: ")
    result = run(option1, option2, number)
    print(result)


def main():
    user_input()


if __name__ == '__main__':
    main()
