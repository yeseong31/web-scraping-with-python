names_data = "김변수,이상수,박참조"
point_data = "100,200,300"
position_data = "공격수,수비수,미드필더"

names_list = names_data.split(',')
point_list = point_data.split(',')
position_list = position_data.split(',')

print(names_list)
print(point_list)
print(position_list)

print('이름\t포인트\t포지션')
members = {}
for name, point, position in zip(names_list, point_list, position_list) :
    print(f'{name}\t{point}\t{position}')
    members[name] = [name, point, position]

print(members)