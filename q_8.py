def one(f):
    # 1
    line = 1
    x = []
    for i in f:
        if line in [1, 2, 5]:
            print("Line {}: {}".format(line, i.strip()))
            x.append(str("Line {}: {}".format(line, i.strip())))

        line += 1

    print(x)


def two(data):
    # 2
    # print("no of line : ", line - 1)
    print(data)
    print(len(data))
    k = []
    for i in data:
        k.append(i.split('.'))
    count = 1
    for i in k:
        for j in i:
            count += 1
            print(j.strip())
    print(count - 1)


def three(data):
    print(data)
    print(len(data))
    k = []
    for i in data:
        k.append(i.split('.'))
    count = 1
    for i in k:
        for j in i:
            for words in j.split():
                if len(words) == 3:
                    print(words.strip())


def four(data):
    k = []
    for i in data:
        k.append(i.split('.'))
    count = 1
    for i in k:
        for j in i:
            for words in j.split():
                if words.isupper():
                    print(words.strip())


def five(data):
    k = []
    for i in data:
        k.append(i.split('.'))
    count = 1
    for i in k:
        for j in i:
            for words in j.split():
                if words.islower():
                    print(words.strip())


def six(data):
    k = []
    for i in data:
        k.append(i.split('.'))
    count = 1
    for i in k:
        for j in i:
            for words in j.split():
                if words.isalpha():
                    print(words.strip())


def seven(data):
    k = []
    dict = {}
    for i in data:
        k.append(i.split('.'))
    count = 1
    for i in k:
        for j in i:
            for words in j.split():
                if words in dict:
                    dict[words] += 1
                else:
                    dict[words] = 1
    return dict


f = open("test.txt", "r")
data = f.readlines()
# one(f)
# two(data)
# three(data)
# four(data)
# five(data)
# six(data)
# print(seven(data))
