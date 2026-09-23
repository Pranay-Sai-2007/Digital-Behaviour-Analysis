import csv

APP = 'instagram'

data = 'digital_behaviour.csv'

insta_minutes = []

with open(data,'r',encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        insta_minutes.append(int(row['Instagram_Minutes']))

last_seven_days = insta_minutes[-1:-8:-1]

print(f"App : {APP} \nTotal : {sum(last_seven_days)} \nAverage : {sum(last_seven_days)//7} \nMaximum : {max(last_seven_days)} \nMinimum : {min(last_seven_days)}")

