from typing import List


def calc(a: int, b: int) -> int:
    return a + b


def to_int(a_list: List[str]) -> List[int]:
    return [int(e) for e in a_list]


if __name__ == '__main__':
    print(to_int(['1', '2']))
