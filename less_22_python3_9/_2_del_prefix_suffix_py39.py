if __name__ == '__main__':

    print("\n=== older version")
    text = 'text'
    text = text.rstrip('xt')
    print(text)

    text2 = 'text2'
    text2 = text2.rstrip('At2')  # ожидаем, что ничего не будет удалено
    print(text2)  # Однако операция удаления букв выполнилась (частично, поэлементно)

    print("\n=== python 3.9 version")
    text = 'text'
    text = text.removesuffix('At')  # удаляет целиком, если такой суффикс есть
    print(text)
    text = text.removeprefix('tEX')  # удаляет целиком, если такой префикс есть
    print(text)
    text = text.removesuffix('t')
    print(text)
    text = text.removeprefix('t')
    print(text)
