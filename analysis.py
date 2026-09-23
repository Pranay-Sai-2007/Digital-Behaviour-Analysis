import numpy as np
import csv

insta_minutes = []
study_minutes = []

data = "digital_behaviour.csv"

with open(data,"r",encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        insta_minutes.append(int(row['Instagram_Minutes']))
        study_minutes.append(int(row['Study_Minutes']))

insta_minutes = np.array(insta_minutes[0:7])
study_minutes = np.array(study_minutes[0:7])

print(f"App : Instagram \nTotal minutes : {np.sum(insta_minutes)} \nAverage minutes : {round(np.mean(insta_minutes))} \nMaximum minutes : {np.max(insta_minutes)} \nMinimum minutes : {np.min(insta_minutes)}\n")

print(f"App : Study \nTotal minutes : {np.sum(study_minutes)} \nAverage minutes : {round(np.mean(study_minutes))} \nMaximum minutes : {np.max(study_minutes)} \nMinimum minutes : {np.min(study_minutes)}\n")

print(insta_minutes)

insta_minutes = np.array(insta_minutes,dtype=float)
insta_hours = insta_minutes / 60
print(f'Instagram Hours : {np.round(insta_hours,2)}\n')

print(study_minutes)

study_minutes = np.array(study_minutes,dtype=float)
study_hours = study_minutes/60
print(f'Study Hours : {np.round(study_hours,2)}')


greater = np.array((insta_minutes[insta_minutes>100]),dtype = int)
print(greater)