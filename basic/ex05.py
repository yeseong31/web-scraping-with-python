names_data = "김변수,이상수,박참조"
point_data = "100,200,300"
position_data = "공격수,수비수,미드필더"

names_list = names_data.split(',')
point_list = point_data.split(',')
position_list = position_data.split(',')

# open('파일명', '모드(쓰기, 읽기, 추가)', 인코딩)
f = open('../files/file01.txt', 'w', encoding='UTF-8-SIG')
for name, point, position in zip(names_list, point_list, position_list) :
    f.write(f'{name}\t{point}\t{position}\n')
f.close()

# CSV(영어: comma-separated values)는 몇 가지 필드를 쉼표(,)로 구분
f2 = open('../files/file02.csv', 'w', encoding='UTF-8-SIG')
for name, point, position in zip(names_list, point_list, position_list) :
    f2.write(f'{name},{point},{position}\n')
f2.close()

f2 = open('../files/file02.csv', 'r', encoding='utf-8-sig')
file_data = f2.read()
print(file_data)
print(type(file_data))
