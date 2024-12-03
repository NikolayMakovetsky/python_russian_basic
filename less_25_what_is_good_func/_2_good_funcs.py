import random


def generate_pin(length: int) -> str:
    return ''.join(str(random.randint(0, 9)) for _ in range(length))


def replace_fives(a_list: list, value: str) -> list[str]:
    """Лучшая практика
    Функция возвращает новый список, а не меняет передаваемый,
    т.о. она максимально независима"""
    return [element.replace('5', value) for element in a_list]


def replace_fives_inplace(a_list: list, value: str):
    """Допустимая практика, но лучше избегать таких решений
    Функция принимает параметр, меняет его и возвращает измененным."""
    for index in range(len(a_list)):
        a_list[index] = a_list[index].replace('5', value)


def write_file(filename: str, data: str):
    with open(filename, 'w') as file:
        file.write(data)


if __name__ == '__main__':
    pins = [generate_pin(8) for _ in range(5)]
    pins_without_fives = replace_fives(pins, '6')
    str_list = '\n'.join(pins_without_fives)
    print(pins_without_fives)
    write_file("test1.txt", str_list)
