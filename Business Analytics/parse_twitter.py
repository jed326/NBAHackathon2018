import pandas as pd
def getnumfollowers(line):
    num = -1
    for i in range(len(line)):
        if (line[i].isdigit()):
            num = int(line[0:i+1])
            continue
        else:
            line = line[i+1:].strip()
            return line, num


followers = {}
for line in open('NBA player twitter follows.txt', 'r'):
    line, num = getnumfollowers(line)
    if(num == -1):
        continue
    names = line.split(",")
    for i in range(len(names)):
        if (i != 0):
            names[i] = names[i][1:]
    for i in range(len(names)):
        followers[names[i]] = num

followers['Kevin Durant'] = 255
print(followers)
print(len(followers))

    
s = pd.Series(followers, index = followers.keys())
s.to_csv('twitter_followers')
