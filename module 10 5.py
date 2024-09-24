import multiprocessing
import datetime as time
def read_info(name):
    all_data = []
    with open(name, 'r', encoding = 'utf-8') as file:
        line = 'line'
        while line is not None:
            line = file.readline()
            all_data.append(line)
    return end - start
filenames = [f'./texts/file {file}.txt' for file in range(1, 5)]
#start = time.datetime.now()
#if __name__ == '__main__':
#    with multiprocessing.Pool(processes = 4) as pool:
#        a = map(read_info, filenames)
#end = time.datetime.now()
#print(f'Времени затрачено: {end - start}')
start = time.datetime.now() #Почему 0?
b = map(read_info, filenames)
end = time.datetime.now()
print(f'Времени затрачено: {end - start}')