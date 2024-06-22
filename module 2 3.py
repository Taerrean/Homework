my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
num = 0
count = 0
while count < len(my_list) - 1: # Минус один, так как даже при невыполнении условия цикл выполняется ещё один раз
    num = my_list[count]
    if num < 0:
        break
    elif num == 0:
        count += 1
        continue
    else:
        print(num)
        count += 1