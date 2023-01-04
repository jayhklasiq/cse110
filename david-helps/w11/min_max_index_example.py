# -----------------------------------------------------------
# Example of how to use min(), max() and index() when
# working with lists
#
# David Ward
# CSE 110 Section 22
# ----------------------------------------------------------- 

# EXTRA - Clears the terminal before the game is played
import os
os.system('cls')

dates = []
temps = []

with open("average_temps.txt") as average_temps_file:
  for line in average_temps_file:
    record = line.strip().split(',')
    dates.append(record[0])
    temps.append(record[1])

# use min() and index() function to get the index of the smallest value
# low = min(temps)
# lowest_index = temps.index(low)

# use max() and index() function to get the index of the smallest value
# high = max(temps)
# highest_index = temps.index(high)

# NOTE: Remember, the above lines (24/25 and 26/27) could have been combined 
# into one. They were only broke apart for simplicity. Here's how they could
# have been written
lowest_index = temps.index(min(temps))
highest_index = temps.index(max(temps))

# print results
print(f"The high temp was {temps[highest_index]} on {dates[highest_index]}")
print(f"The low temp was {temps[lowest_index]} on {dates[lowest_index]}")

