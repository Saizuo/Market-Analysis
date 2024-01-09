import pandas as pd
import matplotlib.pyplot as plt
import sys

df = pd.read_csv('sales.csv')

try:
    color = sys.stdout.shell
except AttributeError:
    raise RuntimeError("Use IDLE")

while True:
    color.write("=" * 110 + "\n", "COMMENT")
    print()
    color.write("""
                                    ███╗   ███╗ █████╗ ██████╗ ██╗  ██╗███████╗████████╗
                                    ████╗ ████║██╔══██╗██╔══██╗██║ ██╔╝██╔════╝╚══██╔══╝
                                    ██╔████╔██║███████║██████╔╝█████╔╝ █████╗     ██║   
                                    ██║╚██╔╝██║██╔══██║██╔══██╗██╔═██╗ ██╔══╝     ██║   
                                    ██║ ╚═╝ ██║██║  ██║██║  ██║██║  ██╗███████╗   ██║   
                                    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝  Analysis                                    
    """, "KEYWORD")
    print()
    color.write("=" * 110 + "\n", "COMMENT")
    color.write("1) Analyze the data\n", "STRING")
    color.write("2) Visualize the data \n", "STRING")
    color.write("3) Manipulate the data\n", "STRING")
    color.write("4) Export The Data\n", "STRING")
    color.write("5) Exit\n", "STRING")
    color.write("=" * 110 + "\n", "COMMENT")
    ch = int(input('Select your Choice [1-5] : '))

    if ch == 1:
            color.write("=" * 110 + "\n", "COMMENT")
            color.write('Data Analysis\n', "COMMENT")
            color.write('1. Show Dataframe\n',"STRING")
            color.write('2. Show N number of records from top \n',"STRING")
            color.write('3. Show N number of records from bottom\n',"STRING")
            color.write('4. Display a particular row of a dataframe\n',"STRING")
            color.write('5. Display a column of a dataframe\n',"STRING")
            color.write('6. Display a combination of rows and columns from a dataframe\n',"STRING")
            color.write('6. Exit\n',"STRING")
            color.write("=" * 110 + "\n", "COMMENT")
            choice = int(input('Select your Choice [1-6] : '))

            if choice == 1:
                print(df)
            elif choice == 2:
                n = eval(input("Enter the number of rows you want to read from the top: "))
                print(df.head(n))
            elif choice == 3:
                n = eval(input("Enter the number of rows you want to read from the bottom: "))
                print(df.tail(n))
            elif choice == 4:
                n = eval(input("Enter the row number you want to display: "))
                print(df.iloc[n])
            elif choice == 5:
                n = eval(input("Enter the column number you want to display: "))
                print(df.iloc[:, n])
            elif choice == 6:
                n = eval(input("Enter the row number you want to display: "))
                m = eval(input("Enter the column number you want to display: "))
                print(df.iloc[n, m])
            elif choice == 7:
                print("Exiting Data Analysis. Goodbye!")
                break

        
    elif ch == 2:
        while True:
            color.write("=" * 110 + "\n", "COMMENT")
            color.write('Data Visualization\n', "COMMENT")
            color.write('1. Plot Line Chart\n',"STRING")
            color.write('2. Plot Bar Chart\n',"STRING")
            color.write('3. Plot Histogram\n',"STRING")
            color.write('4. plot Pie Chart\n',"STRING")
            color.write('5. Plot Scatter Chart\n',"STRING")
            color.write('6. Exit\n',"STRING")
            color.write("=" * 110 + "\n", "COMMENT")
            choice = int(input('Select your Choice [1-6] : '))

            if choice == 1:
                print('Plotting Line Chart...')
                # Example: Plotting a line chart for 'Price' and 'Units_Sold'
                plt.plot(df['Product'], df['Price'], label='Price')
                plt.plot(df['Product'], df['Units_Sold'], label='Units_Sold')
                plt.xlabel('Product')
                plt.ylabel('Values')
                plt.legend()
                plt.show()
            elif choice == 2:
                print('Plotting Bar Chart...')
                # Example: Plotting a bar chart for 'Budget' and 'Revenue'
                plt.bar(df['Product'], df['Budget'], label='Budget')
                plt.bar(df['Product'], df['Revenue'], label='Revenue', alpha=0.5)
                plt.xlabel('Product')
                plt.ylabel('Values')
                plt.legend()
                plt.show()
            elif choice == 3:
                print('Plotting Histogram...')
                # Example: Plotting a histogram for 'Price'
                plt.hist(df['Price'], bins=10, edgecolor='black')
                plt.xlabel('Price')
                plt.ylabel('Frequency')
                plt.show()
            elif choice == 4:
                print('Plotting Pie Chart...')
                # Example: Plotting a pie chart for 'Product' and 'Revenue'
                plt.pie(df['Revenue'], labels=df['Product'], autopct='%1.1f%%', startangle=90)
                plt.axis('equal')
                plt.title('Revenue Distribution by Product')
                plt.show()
            elif choice == 5:
                print('Plotting Scatter Plot')
                # Creating a scatter plot to visualize the relationship between two numerical variables, such as 'Price' and 'Units_Sold'
                plt.scatter(df['Price'], df['Units_Sold'])
                plt.xlabel('Price')
                plt.ylabel('Units Sold')
                plt.title('Scatter Plot: Price vs Units Sold')
                plt.show()
            elif choice == 6:
                print("Exiting Data Visualization. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
    elif ch == 3:
        while True:
            color.write("=" * 110 + "\n", "COMMENT")
            color.write('Data Manipulation\n', "COMMENT")
            color.write('1. Add a row to Dataframe\n"', "STRING" )
            color.write('2. Remove a row to Dataframe\n"', "STRING")
            color.write('3. Add a Column to Dataframe\n"', "STRING")
            color.write('4. Remove a Column to Dataframe\n"', "STRING")
            color.write('. Remove a Column to Dataframe\n"', "STRING")
            color.write("=" * 110 + "\n", "COMMENT")
            ch = int(input("Enter Choice: "))

            if ch == 1: # Add a row to Dataframe
                print("Add a row to Dataframe")
                print(df)
                print("Enter the row you want to add")
                row = input()
                df = df.append(row, ignore_index=True)
                print(df)
            elif ch == 2: # Remove a row to Dataframe
                print("Remove a row to Dataframe")
                print(df)
                print("Enter the row you want to remove")
                row = input()
                df = df.drop(row, axis=0)
                print(df)
            elif ch == 3: # Add a Column to Dataframe
                print("Add a Column to Dataframe")
                print(df)
                print("Enter the column you want to add")
                col = input()
                df = df.append(col, ignore_index=True)
                print(df)
            elif ch == 4: # Remove a Column to Dataframe
                print("Remove a Column to Dataframe")
                print(df)
                print("Enter the column you want to remove")
                col = input()
                df = df.drop(col, axis=1)
                print(df)
            
    elif ch == 4:
        while True:
            color.write("=" * 110 + "\n", "COMMENT")
            color.write("Export The Data\n", "COMMENT")
            color.write("1)Read a csv and Create a DataFrame df\n","STRING")
            color.write("2)Accept the column names which the user wants to include in the  dataframe\n","STRING")
            color.write("3)Accept the number of rows reading from the top of csv to create the dataframe\n","STRING")
            color.write("4)Write the updated dataframe into a new csv file named  sales.csv\n","STRING")
            color.write("=" * 110 + "\n", "COMMENT")
            ch = int(input("Enter Choice: "))
            if ch == 1:
                path = input("Enter the csv file name with path: ")
                pd.set_option('display.max_rows', 500)
                pd.set_option('display.max_columns', 500)
                pd.set_option('display.width', 1000)
                df = pd.read_csv(path)
                print(df)
            elif ch == 2:
                path = input("Enter the csv file name with path: ")
                y = eval(input("Enter the column name you want to include in the dataframe:"))
                df = pd.read_csv(path, usecols=y)
                print(df)
            elif ch == 3:
                path = input("Enter the csv file name with path: ")
                n = eval(input("Enter the number of rows you want to read from the csv: "))
                df = pd.read_csv(path, nrows=n)
                print(df)
            elif ch == 4:
                path = input("Enter the csv file name with path for writing: ")
                df.to_csv(path, index=False)
                print(df)
    elif ch == 5:
        print("Exiting the program")
        break
    else:
        print("Invalid option, please retry")
