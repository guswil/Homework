#Defnitely not the cleanest code...
import csv

f = open('budget_data_1.csv')
csvfile = list(csv.reader(f))
del csvfile[0]

csvmonths = list([csvfile[i][0] for i in range(len(csvfile))])

csvmonths2 = []
print("HEY! Here's you info on these records! \n")

print("Number of months in dataset: " + str(len(csvfile)))
print("Total Revenue in dataset: " + str(sum(csvfile)))

#print("Total Revenue in dataset: " + str(sum(csvfile)))
revs = [int(csvfile[i+1][1]) - int(csvfile[i][1]) for i in range(len(csvfile)-1)]
revs = [0] + revs
usefuldict = dict(zip(csvmonths,revs))

print(sum(revs)/len(revs))

for key, value in usefuldict.items():
    if max(revs[1:]) == value:
        print("The Greatest Revenue increase happened in " + key)
for key, value in usefuldict.items():
    if min(revs[1:]) == value:
        print("The Greatest Revenue drop happened in " + key)
