import pandas

#Using DataFrame to make tables.
df1 = pandas.DataFrame([[2,3,4],[10,20,30]])
print (df1)

#Adding Column Names and Index Name to the Table
df2 = pandas.DataFrame([[2,3,4],[10,20,30]],columns = ["Price","Age","Value"],index = ["First","Second"])
print (df2)

#Making tables using Dictionaries
df3 = pandas.DataFrame([{"Name":"John"},{"Name":"JacK"}])                   #Dictionaries use curly brackets
print (df3)
df4 = pandas.DataFrame([{"Name":"John","Surname":"Jhons"},{"Name":"Jack"}])             #Since there is no surname it shows NaN
print (df4)

#Finding mean of the values in table "df2" through searching in dir(df2)
mean = df2.mean()
print (mean)

#Finding mean of the previous mean
mean_mean = mean.mean()
print (mean_mean)

#Calling value from particular column:
column = df2.Price
print (column)



