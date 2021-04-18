import pandas as pd

data = pd.read_csv('/home/hadoop/PycharmProjects/pythonProject/bank_dataset/bank-additional/bank-additional.csv'
                   , sep=';')


data.columns

#
# ['age', 'job', 'marital', 'education', 'default', 'housing', 'loan',
#        'contact', 'month', 'day_of_week', 'duration', 'campaign', 'pdays',
#        'previous', 'poutcome', 'emp.var.rate', 'cons.price.idx',
#        # 'cons.conf.idx', 'euribor3m', 'nr.employed', 'y']

data.y.value_counts()

# no     3668
# yes     451