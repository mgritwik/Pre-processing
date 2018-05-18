import pandas as pd
import numpy as np

temp=count=0
indices=[]
#get all features whose sequence to be considered
day=atm_name=festival_religion=holiday_sequence=working_day={}
#read data
df=pd.read_csv('newClassesData.csv')
#create a new feature for storing average amount withdrwan for each unique sequence
df['averageAmountWithdrawn']=0
#add all the unique values to list
day=set(df['Weekday'].values.tolist())
atm_name=set(df['ATM Name'].values.tolist())
festival_religion=set(df['Festival Religion'].values.tolist())
holiday_sequence=set(df['Holiday Sequence'].values.tolist())
working_day=set(df['Working Day'].values.tolist())

#for each of the above unique sequence evaluate the average amount withdrawn and store in all of the corresponding rowa
for d in day:
	for a in atm_name:
		for f in festival_religion:
			for h in holiday_sequence:
				for w in working_day:
					count+=1
					indices=np.where((df['Weekday']==d)&(df['ATM Name']==a)&(df['Festival Religion']==f)&(df['Holiday Sequence']==h)&(df['Working Day']==w))
					for each in indices:
						#print(indices)
						avg=df.loc[each]['Total amount Withdrawn'].tolist()
					if(len(avg)!=0):
						avg1=int(np.ceil(sum(avg)/len(avg)))
					else:
						continue
					for each in indices:
						df.at[each,'averageAmountWithdrawn']=avg1	

#store in a .csv file
df.to_csv('newClassesData.csv',sep=',')