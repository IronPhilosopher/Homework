import string
class WordsFinder:
    def __init__(self, *files):
        self.file_names = []
        for i in files:
            self.file_names.append(i)

    def get_all_words(self):
        all_words = {}
        for file in self.file_names:
            value = []
            with open(file, encoding='utf-8') as file1:
                for line in file1:
                    f_line = line.lower().translate(str.maketrans('', '', string.punctuation)).split()
                    for word in f_line:
                        value.append(word)
            all_words.update({file:value})
            return all_words

    def find(self, word):
        dic = self.get_all_words()
        found = {}
        for i in dic.items():
            if word.lower() in i[1]:
                found.update({i[0]:i[1].index(word.lower())+1})
        return found

    def count(self, word):
        dic = self.get_all_words()
        found = {}
        for file in dic.items():
            counter = 0
            for i in file[1]:
                if i == word.lower():
                    counter +=1
            if counter > 0:
                found.update({file[0]: counter})
        return found

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))