a_list = [1, 0, True]

b_list = []

c_list = ['dffd', "", "ffii"]

error_list = ['err1', "", "err456"]

if __name__ == '__main__':
    print("=== all, any")
    print(all(a_list))  # False
    print(any(a_list))  # True

    print("=== all, any if collection is empty")
    print(all(b_list))  # True (при пустой коллекции) ЗДЕСЬ ЧАСТО ПУТАЮТСЯ
    print(any(b_list))  # False

    print("=== all")
    if all(c_list):
        print(c_list)
    else:
        print("c_list includes empty strings -> we can't work with it")

    print("=== any")
    if any(error_list):
        print("error_list is not empty -> we have errors in code")

