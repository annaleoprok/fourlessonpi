NUM = 12345


def sum_for(num):

    s = 0
    for item in str(num):
        s = s + int(item)
    return s

def sum_list(num):
    lst = [int(item) for item in str(num)]
    return sum(lst)

if __name__ == '__main__':
    print(sum_for(NUM))
    print(sum_list(NUM))