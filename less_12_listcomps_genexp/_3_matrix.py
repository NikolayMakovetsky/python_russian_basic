from pprint import pprint

matrix = [list(range(x, x+3)) for x in range(3)]

if __name__ == '__main__':
    pprint(matrix, indent=1, width=15)