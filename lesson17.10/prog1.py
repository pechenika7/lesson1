list_ = list()
f = open('1.txt', 'r', encoding='utf8')
while True:
    item = f.readline()
    if item == '' or item =='\n':
        break
    temp_list = item.split()
    list_.append(temp_list)

for i in list_:
    for j in range(3):
        i[j] = int(i[j])

current_max = list_[0][0] + list_[0][1] + list_[0][2]
current_num = 0
for i in range(len(list_)):
    if list_[i][0] + list_[i][1] + list_[i][2] >= current_max:
        current_max = list_[i][0] + list_[i][1] + list_[i][2]
        current_num = i
print(current_max, current_num)