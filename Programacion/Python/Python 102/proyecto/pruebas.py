import csv
with open('./Python 102/proyecto/world_population.csv', "r+") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    for i in reader:
        print(i)
    