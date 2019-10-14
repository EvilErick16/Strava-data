import csv 
import numpy as np
import matplotlib.pyplot as plt


input_file_name = "test_csv_file.csv"
csv_file = open(input_file_name)

reader = csv.reader(csv_file)
"""
Learning how to use matplotlib here's an examnple  
"""
dateAndTime = []
activityType = []
elapsedTime = []
distance = []
count = 0
for x in reader:
    if count != 0:
        dateAndTime.append(x[1])
        activityType.append(x[3])
        elapsedTime.append(x[5])
        distance.append(x[6])
    count = 1


numberOfActivities = len(dateAndTime)
ind = np.arange(numberOfActivities)
width = 0.5
p1 = plt.bar(ind, elapsedTime, width)
p2 = plt.bar(ind, 1, width, bottom=elapsedTime)

plt.ylabel("Elapsed time")
plt.title("Time spent running")
plt.xticks(ind, ("22 Feb", "20 Feb", "23 Feb", "23 Feb", "23 Feb", "25 Feb", "25 Feb"))
plt.yticks(np.arange(0, 25, 1))
#plt.legend(p1[0], "Seconds")


plt.show()

"""
N = 5
menMeans = (20, 35, 30, 35, 27)
womenMeans = (25, 32, 34, 20, 25)
menStd = (2, 3, 4, 1, 2)
womenStd = (3, 5, 2, 3, 3)
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, menMeans, width, yerr=menStd)
p2 = plt.bar(ind, womenMeans, width,
             bottom=menMeans, yerr=womenStd)

plt.ylabel('Scores')
plt.title('Scores by group and gender')
plt.xticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5'))
plt.yticks(np.arange(0, 81, 10))
plt.legend((p1[0], p2[0]), ('Men', 'Women'))

plt.show()
"""