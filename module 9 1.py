def apply_all_func(int_list, *functions):
    operations_dict = {}
    for i in functions:
        result = i(int_list)
        try:
            operations_dict.update({i.__name__: result})
        except TypeError:
            print('Что-то пошло не так, проверьте введённые данные и функции')
    return operations_dict
def factorial(num_list): # Отсебятина
    end_list = []
    for i in num_list:
        s = 1
        for j in range(1, i + 1):
            s *= j
        end_list.append(s)
    return end_list
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted, factorial))