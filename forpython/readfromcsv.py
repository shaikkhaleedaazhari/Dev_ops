import csv
with open('f4.csv') as f:
    csv_reader = csv.reader(f,delimiter=',')
    linecount = 0
    for i in csv_reader:
        print(f'{i}')