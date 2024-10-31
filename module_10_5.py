from datetime import datetime
from multiprocessing import Pool
def read_info(name):
    all_data = []
    with open(name, encoding='utf-8') as file:
        for line in file:
            file.readline()
            all_data.append(line)

files = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']
ts = datetime.now()
read_info(files[0])
read_info(files[1])
read_info(files[2])
read_info(files[3])
te = datetime.now()
print(te-ts)

if __name__ == '__main__':
    ts1 = datetime.now()
    with Pool() as i:
        i.map(read_info, files)
    te1 = datetime.now()
    print(te1 - ts1)