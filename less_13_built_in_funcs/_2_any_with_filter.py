a_list = [0, 0, 1, 0, True, "df"]

if any(a_list):
    print(list(filter(None, a_list)))  # filter with None returns only truthy elements
    print([e for e in a_list if e])
    

if __name__ == '__main__':
    pass
