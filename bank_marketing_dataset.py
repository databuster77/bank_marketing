import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

data = pd.read_csv('/home/hadoop/PycharmProjects/pythonProject/bank_dataset/bank-additional/bank-additional-full.csv'
                   , sep=';')


data.columns

#
# ['age', 'job', 'marital', 'education', 'default', 'housing', 'loan',
#        'contact', 'month', 'day_of_week', 'duration', 'campaign', 'pdays',
#        'previous', 'poutcome', 'emp.var.rate', 'cons.price.idx',
#        # 'cons.conf.idx', 'euribor3m', 'nr.employed', 'y']

data.y.value_counts()

# no     36548
# yes     4640

data.info()

# RangeIndex: 41188 entries, 0 to 41187
# Data columns (total 21 columns):
#  #   Column          Non-Null Count  Dtype
# ---  ------          --------------  -----
#  0   age             41188 non-null  int64
#  1   job             41188 non-null  object
#  2   marital         41188 non-null  object
#  3   education       41188 non-null  object
#  4   default         41188 non-null  object
#  5   housing         41188 non-null  object
#  6   loan            41188 non-null  object
#  7   contact         41188 non-null  object
#  8   month           41188 non-null  object
#  9   day_of_week     41188 non-null  object
#  10  duration        41188 non-null  int64
#  11  campaign        41188 non-null  int64
#  12  pdays           41188 non-null  int64
#  13  previous        41188 non-null  int64
#  14  poutcome        41188 non-null  object
#  15  emp.var.rate    41188 non-null  float64
#  16  cons.price.idx  41188 non-null  float64
#  17  cons.conf.idx   41188 non-null  float64
#  18  euribor3m       41188 non-null  float64
#  19  nr.employed     41188 non-null  float64
#  20  y               41188 non-null  object
# dtypes: float64(5), int64(5), object(11)

num_vars=data.select_dtypes(exclude='object').columns

str_vars=data.select_dtypes(include='object').columns


data_1=data.copy()

job_order=data.job.unique().sort(reversed=False)
job_order=sorted(job_order,reverse=True)

fig, axes = plt.subplots(1, 2, figsize=(15, 5), sharey=False)
sns.histplot(ax=axes[1,0],x=data.age)
sns.histplot(ax=axes[0,0],x=data.duration)
plt.show()


fig, axes = plt.subplots(1, 2, figsize=(15, 5), sharey=False)
sns.histplot(ax=axes[1],x=data.age)
sns.histplot(ax=axes[0],x=data.duration)
plt.show()

plt.subplot(1,2,1)
sns.histplot(x=data.job)
plt.xticks(range(len(job_order)),job_order,rotation=45)
plt.title('plot_1')
plt.subplot(1,2,2)
sns.histplot(x=data.job)
plt.xticks(rotation=45)
plt.title('plot_2')





sns.histplot(data,x='job')
plt.xticks(rotation=45)
plt.show()



g=sns.FacetGrid(data=data_1,col='y',xlim=(0,1500))
g.map(sns.histplot,"duration")




g=sns.PairGrid(data=data_1,vars=num_vars)
g.map_diag(sns.histplot)
g.map_offdiag(sns.scatterplot)
g.tight_layout()

sns.pairplot(data=data_1)

sns.histplot(data,x='duration')

