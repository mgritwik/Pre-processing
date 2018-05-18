import pandas as pd

#dataset having categorical values
df=pd.read_csv('ClassificationData.csv')
# print(df.index,'#########',len(df.index))

#multi-class labels
class_vector=set(df['class'].values.tolist())
#to check the number of unique values and the range of values in them
print('length',len(class_vector),'#############',class_vector)

#initialization and creation of new columns,each unique value being a new label for one hot representation
for i in class_vector:
	df[i]=0

#one-hot conversion of class
for i in df.index:
	temp=df.iloc[i]['class']
	df.at[i,temp]=1

#writing again into a new .csv file
df.to_csv('ClassificationDataOneHot.csv',sep=',')


