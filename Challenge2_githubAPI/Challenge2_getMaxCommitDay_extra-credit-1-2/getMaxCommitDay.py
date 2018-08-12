import json
import matplotlib.pyplot as plt
import numpy as np

# import data
with open('d3_commit-activity.json') as f:
    data = json.load(f)

# write function to get max commit count and week
def getMaxCommit(commit_activity):
    
    # initialize variables to store sum and max
    sumCommitByDay = [0, 0, 0, 0, 0, 0, 0]
    maxCommit = 0
    maxCommitDay = 0
    
    # loop through json and add up commits for each day
    for i in range(0, len(commit_activity)):
        for j in range(0, 7):
            sumCommitByDay[j] = sumCommitByDay[j] + commit_activity[i]["days"][j]
            if sumCommitByDay[j] > maxCommit:
                maxCommit = sumCommitByDay[j]
                maxCommitDay = j
    
    # map of days of the week
    weekday = ["Sun", "Mon", "Tues", "Wed", "Thu", "Fri", "Sat"]
    
    # graph commits by day of the week
    x = np.array([0, 1, 2, 3, 4, 5, 6])
    y = np.array(sumCommitByDay)
    plt.xticks(x, weekday)
    plt.scatter(x, y)
    plt.grid()
    plt.title('Total of Commits by Day of Week in Past Year')
    plt.xlabel('Day of Week')
    plt.ylabel('# of Commits')
    plt.show()
    
    # return results
    return {
        "maxCommit": maxCommit,
        "maxCommitDay": weekday[maxCommitDay],
        "sumCommitByDay": sumCommitByDay
    }

res = getMaxCommit(data)
print(res)