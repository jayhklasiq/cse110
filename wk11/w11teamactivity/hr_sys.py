import os
os.system('cls')

with open('wk11\w11teamactivity\hr_system.txt') as hr_systems:
    for hr_member in hr_systems:
        hr_member = hr_member.strip().split()
        name = hr_member[0]
        identity = hr_member[1]
        job_title = hr_member[2]
        salary = hr_member[3]
        # print(hr_member)
        print(f'Name: {name} (ID: {identity})\t\tJob Title: {job_title} - ${float(salary)/24:.2f}')