import string
class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)
    def get_all_words(self):
        words_dict = {}
        for i in self.file_names:
            with open(i, encoding = 'utf-8') as file:
                all_lines = []
                for line in file:
                    for p in string.punctuation:
                        if p in line:
                            line = line.replace(p, '')
                    line = line.lower().split()
                    for j in line:
                        all_lines.append(j)
                words_dict.update({i: all_lines})
        return words_dict
    def find(self, word):
        find_dict = {}
        for keys, values in self.get_all_words().items():
            for i in range(len(values)):
                if word.lower() == values[i]:
                    find_dict.update({keys: i + 1})
                    break
        return find_dict
    def count(self, word):
        find_dict = {}
        s = 0
        for keys, values in self.get_all_words().items():
            for i in range(len(values)):
                if word.lower() == values[i]:
                    s += 1
            find_dict.update({keys: s})
        return find_dict
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
