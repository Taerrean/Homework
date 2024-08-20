from pprint import pprint
def custom_write(file_name, strings):
    file = open(file_name, 'a', encoding = 'utf-8')
    s = 1
    strings_positions = {}
    for i in strings:
        strings_positions.update({(s, file.tell()): i})
        file.write(f'{i}\n')
        s += 1
    file.close()
    return strings_positions
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('txtfile.txt', info)
for elem in result.items():
  print(elem)