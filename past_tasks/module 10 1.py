from time import sleep
from threading import Thread
def write_words(word_count, file_name):
    with open(file_name, 'a', encoding='utf-8') as file:
        for i in range(1, word_count + 1 ):
            file.write(f'Какое-то слово №{i}\n')
            sleep(0.1)
write_words(10, 'example1.txt')
thr1 = Thread(target = write_words, args = (10, 'example2.txt'))
thr1.start()