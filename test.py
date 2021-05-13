text = input('Вежтите числа через пробел>')
result = []

list = text.split(' ')
for i in range(len(list)):
    print(i)
    if list.index(list[i]) > -1 and list.index(list[i]) != i:
        print(list[i])
        if result.index(list[i]) < 0:
            result.append(list[i])

print('result:', result, 'list:', list)

