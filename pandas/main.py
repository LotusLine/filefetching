import pandas as pd

print('---------------------------------------------------------')

#create a dictionary which contains information about fruits
fruit_dict = {"Name":['Mango', 'Apple','Banana','Peach'], "Quantity": [1,4,8,12]}

#create a dataframe
df = pd.DataFrame(fruit_dict, index=['Series1','Series2','Series3','Series4' ])

print("\n\t\tDataframe From Dictionary\n")
print('---------------------------------------------------------')
print(df)
print('---------------------------------------------------------')




#create a data frame from a list of tuples
#List of Tuples stands for each element in the list as tuple
book_data = [('Python for beginners', 'Hilary', 900, 2),
            ('Aab-e-Hayat', 'Umera', 600, 8),
            ('Super Economies', 'Raghav Bahal', 400, 90)]
            
#dataframe created from list of tuples
df1 = pd.DataFrame(book_data, columns=['Name', 'Author', 'Price', 'Quantity'])



print("\n\t\tDataframe From List of Tuples\n")
print('---------------------------------------------------------')
print(df1)
print('---------------------------------------------------------')


#create dataframe from list of dictionaries
book_data = [{'Name':'Python for Beginners','Author':'Hilary','Price':900,'Quantity':2},
             {'Name':'Aab-e-Hayat','Author':'Umera','Price':600,'Quantity':8},
             {'Name': 'Super Economies', 'Author': 'Raghav Bahal', 'Price': 400, 'Quantity':90},
             {'Name': 'True Colors', 'Author': 'Adam Gilchrist', 'Price': 500, 'Quantity': 70},]
 
 
 
#pass the book_data as an argument
df3 = pd.DataFrame(book_data)

print("\n\t\tDataframe From List of Dictionaries\n")
print('---------------------------------------------------------')
print(df3)
print('---------------------------------------------------------')



#Read CSV file for Dataframe
books_data = pd.read_csv("testfile.csv")

#Pass books data as an argument
df4 = pd.DataFrame(books_data)


print("\n\t\tDataframe From List CSV\n")
print('---------------------------------------------------------')
print(df4)
print('---------------------------------------------------------')




#Read Excelfile for Dataframe
excel_data = pd.read_excel("testfile.xls", "Sheet1")

#Pass books data as an argument
df5 = pd.DataFrame(books_data)


print("\n\t\tDataframe From Excel file\n")
print('---------------------------------------------------------')
print(df5)
print('---------------------------------------------------------')