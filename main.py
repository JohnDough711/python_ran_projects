# This is a sample Python script.

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
   # print(f'Hi, {name}')  # Press F9 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
  #  print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import pandas
import csv

#with open('weather_data.csv') as data_file:
 #   data = csv.reader(data_file)
  #  temperatures = []
   # for row in data:
    #    if row[1] != 'temp':
     #       temperatures.append(int(row[1]))

#print(temperatures)

data = pandas.read_csv('weather_data.csv')

monday = data[data.day == 'Monday']
print(monday.temp[0])