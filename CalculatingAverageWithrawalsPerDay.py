# To calculate average withdrawal per day
import pandas as pd

#readFile
df=pd.read_csv('AggregatedData.csv')
#create a new feature and initialze to 0
df['AvgAmountPerWithdrawal']=0

#read the two features and store the evaluated result in the new feature for each position
for i in df.index:
	df.at[i,df.iloc[i]['AvgAmountPerWithdrawal']]=int(df.iloc[i]['Total amount Withdrawn']/df.iloc[i]['No Of Withdrawals'])

#write to a .csv file
df.to_csv('AggregatedDataNew.csv',sep=',')
