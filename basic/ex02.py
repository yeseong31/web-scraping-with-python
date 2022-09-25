string_data = '   www python org   '

print(f'raw data : AA{string_data}AA')
print(f'strip() : AA{string_data.strip()}AA')

string_data = string_data.strip()
print(f'raw data : AA{string_data}AA')

print(f'replace() : {string_data.replace(" ",".")}')
string_data = string_data.replace(" ",".")

string_data = string_data.split(".")
print(f'split() : {string_data}')
print(f'type(string_data) : {type(string_data)}')