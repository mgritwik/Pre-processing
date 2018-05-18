import numpy as np
import pandas as pd
#read Data
df=pd.read_csv('processedCUBdata1.csv')
#df.drop(['Transaction Date'],1,inplace=True)
#conversion of continous values to categorical values by reounding of to ceil 50,000 to (not nearest 50k, avoid shortage of money)
for i in df.index:
	tmp=df.iloc[i]['Total amount Withdrawn']
	if tmp%50000==0:
		roundedtmp=tmp
	else:
		roundedtmp=tmp+50000
		tmp=roundedtmp%50000
		roundedtmp-=tmp
	df.at[i,'Rounded Amount Withdrawn']=roundedtmp

#for building up the classes for converitng the regression problem into a classification problem
#read all the unique values
xlist=list(set(df['Rounded Amount Withdrawn'].values.tolist()))
xlist.sort()

#create classes from the rounded values
df['class']=0
for i in df.index:
	df.at[i,'class']=xlist.index(df.iloc[i]['Rounded Amount Withdrawn'])+1

#write into a .csv file

df.to_csv('processedCUBdata1.csv',sep=',')