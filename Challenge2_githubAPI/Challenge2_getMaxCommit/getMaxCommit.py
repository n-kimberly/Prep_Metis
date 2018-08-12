import json
from pprint import pprint

# import data
with open('d3_commit-activity.json') as f:
    data = json.load(f)

# write function to get max commit count and week
def getMaxCommit(commit_activity):
    
    # initialize variables to store max
    maxCommit = 0
    maxCommitWeek = 0
    
    for i in range(0, len(commit_activity)):
        commit = commit_activity[i]
        if commit["total"] > maxCommit:
            maxCommit = commit["total"]
            maxCommitWeek = commit["week"]
    
    # calculate # of weeks ago to put week val into perspective
    weeksAgo = int(maxCommitWeek)/(365*24*60*60)
    
    # print result
    print("maximum number of commits in this repo is " + str(maxCommit) + ", which occurred on week " + str(maxCommitWeek) + ". This was " + str(52-int(weeksAgo)) + " weeks ago.")
    
    # return max count and max week    
    return {
        "max commit count": maxCommit,
        "max commit week": maxCommitWeek
    }

res = getMaxCommit(data)
print(res)