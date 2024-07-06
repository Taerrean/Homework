def calculate_structure_sum(data_structure):
    counter = 0
    for i in data_structure:
        if isinstance(i, list):
            counter += calculate_structure_sum(i)
        if isinstance(i, dict):
            for key, value in i.items():
                if isinstance(key, tuple):
                    counter += calculate_structure_sum(key)
                if isinstance(key, int):
                    counter += key
                if isinstance(key, float):
                    counter += key
                if isinstance(key, str):
                    counter += len(key)
                if isinstance(key, bool):
                    counter += len(str(key))
                if isinstance(value, list):
                    counter += calculate_structure_sum(value)
                if isinstance(value, dict):
                        counter += calculate_structure_sum(value)
                if isinstance(value, set):
                    counter += calculate_structure_sum(tuple(value))
                if isinstance(value, tuple):
                    counter += calculate_structure_sum(value)
                if isinstance(value, int):
                    counter += value
                if isinstance(value, float):
                    counter += value
                if isinstance(value, str):
                    counter += len(value)
                if isinstance(value, bool):
                    counter += len(str(value))
        if isinstance(i, set):
            counter += calculate_structure_sum(tuple(i))
        if isinstance(i, tuple):
            counter += calculate_structure_sum(i)
        if isinstance(i,int):
            counter += i
        if isinstance(i, float):
            counter += i
        if isinstance(i, str):
            counter += len(i)
        if isinstance(i, bool):
            counter += len(str(i))
    return counter
data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(result)