string_data = 'www.python.org'

index = string_data.find('w')
print(f'문자열의 인덱스 : {index}')
index = string_data.find('.')
print(f'문자열의 인덱스 : {index}')
index = string_data.find('.', 4)
print(f'문자열의 인덱스 : {index}')
index = string_data.find('T')
print(f'문자열의 인덱스 : {index}')

print(f'count(w) : {string_data.count("w")}')
print(f'count(.org) : {string_data.count(".org")}')
print(f'count(T) : {string_data.count("T")}')

string_data = 'Www.pyThon.orG'
print(f'upper() : {string_data.upper()}')
print(f'lower() : {string_data.lower()}')
print(f'string_data : {string_data}')
