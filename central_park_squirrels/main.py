import pandas as pd



data = pd.read_csv('Squirrel_Data.csv')
gray_squirrel_count = len(data[data['Primary Fur Color'] == 'Gray'])
cinnamon_squirrel_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squirrel_count = len(data[data['Primary Fur Color'] == 'Black'])

data_dict = {
    'color' : ['Gray', 'Cinnamon', 'Black'],
    'count' : [gray_squirrel_count,cinnamon_squirrel_count, black_squirrel_count],
}

df = pd.DataFrame(data_dict)

df.to_csv('squirrel_count.csv')