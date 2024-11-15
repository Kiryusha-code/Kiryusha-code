""" def read_last(lines, file = open('c:/Users/Public/article.txt')):    file = file.readlines()
    for i in range(lines, 0, -1):        print(file[-(i)])
lines = int(input())
read_last(lines) """
""" def longest_word(file = open('c:/Users/Public/article.txt').readlines()):    l_w = [' ']
    for i in range(len(file)):        file[i] = file[i].ljust(len(file[i]) + 1, ' ')
        file[i] = file[i].rjust(len(file[i]) + 1, ' ')        counter = 0
        for j in range(len(file[i])):            if file[i][j] == ' ' and j != len(file[i]) - 1:
                word = ''                while file[i][j + 1] != ' ':
                    counter += 1                    word += file[i][j + 1]
            if len(word) > len(l_w[0]):                l_w[0] = word
                if len(l_w) > 1:
                    for k in range(len(l_w), 0, -1):                        l_w = l_w.pop(k)
            if len(word) == len(l_w[0]):                l_w.append(word)
    return l_w
print(longest_word()) """