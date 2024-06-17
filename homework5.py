immutable_var = 12, 'Taerrean', False, 3.1
print('Immutable tuple:', immutable_var)
# immutable_var[0] = 5 не сработает, т.к. кортежи не поддерживают их изменение
mutable_list = ['I', 'love', 'Python']
mutable_list[2] = 'Gaming'
mutable_list[0] = 'We'
print('Mutable list:', mutable_list)