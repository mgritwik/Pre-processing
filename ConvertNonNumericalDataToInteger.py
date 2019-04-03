import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import numpy 
from sklearn.cluster import KMeans
from sklearn import preprocessing	# no cross_validation is required because it's a unsupervised learning algorithm
import pandas


df = pandas.read_excel('ClassificationData.csv')
#print(df.head())
#notice there is non-integer data hence categories in sets of data and convert them into integers
df.convert_objects(convert_numeric=True)
df.fillna(0, inplace=True)


#functionto convert non numerical data to numerical data
def handle_non_numerical_data(df):
	columns=df.columns.values		#returns all the names of the columns

	for column in columns:
		text_digit_vals={} #dictinary to store the mappings example {'female':0,'male':1}
		def convert_to_int(val):
			return text_digit_vals[val] 	#this returns the value of the int that val has been mapped to
	
		if df[column].dtype!=numpy.int64 and df[column].dtype!=numpy.float64:	#if datatype of column is not int/float then:
			column_contents=df[column].values.tolist()					#get all the column contents(all possible values present in the column and form a list)
			#print(column_contents) #to see what is printed
			unique_elements=set(column_contents)						#to get all the unique elements of the above list
			x=0
			for unique in unique_elements:
				if unique not in text_digit_vals:						#if unique not in text value,i,e: if not predefined in the text_didgit_vals list hen define ot right now
					text_digit_vals[unique]=x
					x+=1

			df[column]=list(map(convert_to_int,df[column]))		#inbuilt map functin in pandas to map the values of df[column] to its corresponding convert_to_int function
			#map(aFunction, aSequence) function applies a passed-in function to each item in an iterable object and returns a list containing all the function call results.
	return df

df=handle_non_numerical_data(df)
print(df.head())
