import os
os.system('cls')


entity = []
code = []
year = []
life_expectancy = []
year_of_interest = ''
#Download the dataset
with open('life-expectancy.csv') as data_file:
    # Load the dataset in your Python program
    for data in data_file:
        # Iterate through the data line by line
        data = data.strip().split(',')
        # Split each line into parts
        entity.append(data[0])
        code.append(data[1])
        year.append(int(data[2]))
        life_expectancy.append(float(data[3]))

# print (f'{entity} - {code} - {year} - {life_expectancy}')
        min_life_expectancy = life_expectancy.index(min(life_expectancy))
        max_life_expectancy = life_expectancy.index(max(life_expectancy))
print(f'The overall maximum life expectancy is: {life_expectancy[max_life_expectancy]} from {entity[max_life_expectancy]} in {year[max_life_expectancy]}')
print(f'The overall minimum life expectancy is: {life_expectancy[min_life_expectancy]} from {entity[min_life_expectancy]} in {year[min_life_expectancy]}')
print()

total = 0
for each_life_expectancy in life_expectancy:
        total += each_life_expectancy
total_figure = len(life_expectancy)
average = total /total_figure
print(f'The average life expectancy across all countries was: {average:.2f}')
year_of_interest = (input('What is your year of interest? '))

for index in range(len(year)):
         if year == year_of_interest[index]:
                min_life_expectancy_in_year_of_interest = life_expectancy[index].index(min(life_expectancy[index]))
                max_life_expectancy_in_year_of_interest = life_expectancy[index].index(max(life_expectancy[index]))
