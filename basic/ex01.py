string_data = 'www.python.org'

# find() : 문자열안에서 문자열 찾아 인덱스를 반환을 원해
index = string_data.find('w')
index = string_data.find('.')
index = string_data.find('.', 4)
# 찾을 문자열이 없다면 -1
index = string_data.find('T')
print(f'문자열의 인덱스 : {index}')

# count() : 문자열안에서 문자열을 찾아 개수를 반환
print(f'count(w) : {string_data.count("w")}')
print(f'count(.org) : {string_data.count(".org")}')
print(f'count(T) : {string_data.count("T")}')

string_data = 'Www.pyThon.orG'
print(f'upper() : {string_data.upper()}')
print(f'lower() : {string_data.lower()}')
print(f'string_data : {string_data}')
