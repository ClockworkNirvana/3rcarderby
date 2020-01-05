import math
import csv
import operator


def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier


# change this value to the number of different scoring bands needed
bands = 30
teams = 0
i = 1
a = 0
b = 1

with open('results.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        teams += 1

# Number of teams per band (average)
npb = round_down(teams/bands)
extra = teams % bands
amt_band = []
standings = []

# setting amt_band to number of teams per band
while bands >= i:
    a = npb
    # any extra teams not cleanly divided are spread over the top few bands
    if extra >= b:
        a += 1
        b += 1
    amt_band.append(a)
    a = 0
    i +=1

reader = csv.reader(open("results.csv", encoding='utf-8-sig'), delimiter=",")
sortedlist = sorted(reader, key=lambda row: int(row[1]), reverse=True)

writer = csv.writer(open('scores.csv', 'w', encoding='utf-8-sig', newline=''), delimiter=",")
max_num = 0
in_grp = 0
band_num = bands
counter = 0
for band in amt_band:
    while in_grp < band:
        print([str(sortedlist[counter][0]), str(band_num)])
        writer.writerow([str(sortedlist[counter][0]), str(band_num)])
        counter += 1
        in_grp += 1
    in_grp = 0
    band_num -=1
