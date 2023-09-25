#1.Adding record for csv file
header=['Prod_No','Prod_Name','Jan','Feb','Mar','Apr','May','Jun']
# 5 product details print in csv file directly
rows=[
    [1,'scanner',8500,8000,9600,10000,1100,1450],
    [2,'cpu',5000,4000,13000,6800,16000,6600],
    [3,'Monitor',10000,15500,17000,4000,7500,1000],
    [4,'mouse',39000,36000,54000,46000,42000,30000],
    [5,'keybord',4900,4600,7500,8000,9500,9000]
     ]
# create empty list to store more 7 product details from user input
l=[] 
for i in range(7):
    n=int(input('Enter Product Id:'))
    name=input('Enter Product Name:')
    jan=int(input('Enter Jan Month Selling:'))
    feb=int(input('Enter Feb Month Selling:'))
    mar=int(input('Enter March Month Selling:'))
    apr=int(input('Enter April Month Selling:'))
    may=int(input('Enter May Month Selling:'))
    jun=int(input('Enter Jun Month Selling:'))
data=[n,name,jan,feb,march,april,may,jun]
l.append(data)
insert.writerows(l)

 #2.Create DATAFRAME
df=pd.read_csv(file)
print(df)

#3.Change Column Name
df.columns=['Product No','Product Name','January','February','March','April','May','June']
print(df)

#4.Add column "Total Sell" to count total of all month and "Average Sell"
df['Total Sell']=df['January']+df['February']+df['March']+df['April']+df['May']+df['June']
print(df)

#5.Add 2 row at the end.
len(df)
df.loc[12]=[13,'Camera',4500,6000,10000,9500,8500,8000,46500]
df.loc[13]=[14,'Head-phone',6500,7200,3600,4500,9000,6000,36800]
print(df)

#6.Add 2 rows after 3rd row.
header=['Product No', 'Product Name', 'January', 'February', 'March', 'April', 'May', 'June','Total','Average']
df.loc[2.5] = [15, 'cable',1290,7128,7456,4325,3874,2002,26075,4345.8333333]
df = df.sort_index().reset_index(drop=True)
df.loc[3.5] = [16, 'projecter',1140,1148,2260,2245,2256,2221,11270,1878.333333]
df = df.sort_index().reset_index(drop=True)

#7.Display first 5 rows
print(df.head())

#8.Display Last 5 rows
print(df.tail())

#9.Display row 6 to 10
print(df.loc[6:10])

#10.Display only Product Name
print(df['Product Name'])

#11.Print Sell Of January Month With Product id and Product Name
print(df[['January','Product No','Product Name']])

#12.print only those Product No,Product Name where January Sell>5000 and February>8000
print(" record based on condition")
df["January"] = pd.to_numeric(df["January"])
df["February"] = pd.to_numeric(df["February"])
df2 = df[(df["January"] > 5000) & (df["February"] > 8000)]
print(df2[["Product No", "Product Name"]])

#13.Print Record in sorting order of Product Name
print(df.sort_values(by="Product Name"))

#14.display in a odd index number
print(df.loc[1::2])

#15.Print Alternate row.
print(df.loc[::2])






