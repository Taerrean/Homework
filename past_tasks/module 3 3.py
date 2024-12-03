def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)
print_params(12)
print_params(15,'23')
print_params(b = 25)
print_params(c = [1,2,3])
values_list = [0, '1', 5.2]
values_dict = {'a': False, 'b': 42, 'c': 'string'}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [3, 1]
print_params(*values_list_2)