from ex_html import get_html

data = get_html()
# html 형석의 데이터를 문자열로 찾아서 작업하는 것은 괴롭다.
print(data)
print(data.find('신'))
print(data.find('는'))
data2 = data[data.find('신'):data.find('는') + 1]
print(data2)
