from sqlite3.dbapi2 import apilevel

text = 'hello world'

# set
unique_letters = {letter for word in text.split() for letter in word if letter<'o'}

# dict
alphabet = {index: letter for index, letter in enumerate('abcdefghijklmnopqrstuvwxyz', 1)}

if __name__ == '__main__':
    print(unique_letters)
    print(alphabet)
    print({v: k for k, v in alphabet.items()})