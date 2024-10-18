import multiprocessing
import time
def read_info(name):
    all_data = []
    with open(name, 'r', encoding = 'utf-8') as file:
        line = 'line'
        while line is not None:
            line = file.readline()
            all_data.append(line)
    return all_data
filenames = [f'./texts/file {file}.txt' for file in range(1, 5)]
#start = time.time()
#if __name__ == '__main__':
#    with multiprocessing.Pool(processes = 4) as pool:
#        a = map(read_info, filenames)
#end = time.time()
#print(f'Времени затрачено: {end - start}')
start = time.time() #Почему 0?
b = map(read_info, filenames)
for i in b:
    pass
end = time.time()
print(f'Времени затрачено: {end - start}')