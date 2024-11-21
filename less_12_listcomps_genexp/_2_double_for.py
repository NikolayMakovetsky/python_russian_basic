text = 'hello world'
letters = [letter for word in text.split() for letter in word if letter<'l']

if __name__ == '__main__':
    print(letters)
