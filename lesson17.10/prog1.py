list_ = list()
f = open('1.txt', 'r', encoding='utf8')
while True:
    item = f.readline()
    if item == '' or item == '\n':
        break
    temp_list = item.split()
    list_.append(temp_list)

for i in list_:
    for j in range(3):
        i[j] = int(i[j])

current_max = sum(list_[0])
current_num = 0
for i in range(len(list_)):
    if sum(list_[i]) >= current_max:
        current_max = sum(list_[i])
        current_num = i
print(current_max, current_num)
for num, l in enumerate(list_):
    print(num+1, ':', l) 