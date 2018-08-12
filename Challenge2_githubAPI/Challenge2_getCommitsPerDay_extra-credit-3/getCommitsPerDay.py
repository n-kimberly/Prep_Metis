import json
import matplotlib.pyplot as plt
import numpy as np

# import data
with open('d3_commit-activity.json') as f:
    data = json.load(f)

# write function to get max commit count and week
def getCommitsPerDay(commit_activity):
    
    # initialize variables to store sum and max
    count = 0
    x = [0]   
    y = [0]
    y_cum = [0]
    
    # loop through json and store commit #
    for i in range(0, len(commit_activity)):
        for j in range(0, 7):
            prev = int(y_cum[count])
            curr = int(commit_activity[i]["days"][j])
            y.append(curr)
            y_cum.append(prev + curr)
            x.append(count)
            count += 1
            
    # graph commits per day since last year
    plt.scatter(x, y, color='blue')
    plt.grid()
    plt.title('Daily Commits in Past Year')
    plt.xlabel('Day')
    plt.ylabel('# of Commits')
    plt.show()
    
    # graph cumulative commits per day since last year
    plt.scatter(x, y_cum, color='red')
    plt.grid()
    plt.title('Cumulative Commits in Past Year')
    plt.xlabel('Day')
    plt.ylabel('# of Commits')
    plt.show()
    
    # calculate some stats
    std = np.std(y)
    avg = np.mean(y)
    
    # return results
    return {
        "avg commits/day": str(round(avg, 3)),
        "std of commits/day": str(round(std, 3))
    }

res = getCommitsPerDay(data)
print(res)
