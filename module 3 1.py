calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()
    a = len(string)
    b = string.upper()
    c = string.lower()
    return (a, b, c)
def is_contains(string, list_to_search):
    count_calls()
    for i in list_to_search:
        if string.lower().strip() in i.lower().strip():
            return True
        else:
            return False
list = []
a = int(input('Введите кол-во строк '))
for i in range(a):
    string = input('Введите строку ')
    print(string_info(string))
    list.append(string)
line = input('Введите искомую строку ')
print(is_contains(line, list))
print(calls)