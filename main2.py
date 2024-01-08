import pandas as pd 
import matplotlib.pyplot as plt
import sys

df = pd.read_csv('sales.csv')

try:
    color = sys.stdout.shell
except AttributeError:
    raise RuntimeError("Use IDLE")

while True:
    color.write("="*110 + "\n", "COMMENT")
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
    color.write("="*110 + "\n", "COMMENT")
    color.write("1) Analyze the data\n", "STRING")
    color.write("2) Visualize the data \n", "STRING")
    color.write("3) Manipulate the data\n", "STRING")
    color.write("4) Export The Data\n", "STRING")
    color.write("5) Exit\n", "STRING")
    
    ch = int(input('Select your Choice [1-5] : '))

    if ch == 1:
        print("1")
        
    elif ch == 2:
                while True:
                    print("=" * 100)
                    color.write('Data Visualization',"COMMENT")
                    print('1. Plot Line Chart')
                    print('2. Plot Bar Chart')
                    print('3. Plot Histogram')
                    print('4. Exit')
                    print("=" * 100)
                    
                    choice = int(input('Select your Choice [1-4]: '))
                    
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
                        print("Exiting Data Visualization. Goodbye!")
                        break

                    else:
                        print("Invalid choice. Please enter a number between 1 and 4.")
    elif ch == 3:
        print("3")
        # Additional code for option 3 can be added here
        
    elif ch == 4:
         while True:
          print("1)Read a csv Student.csv and Create a DataFrame stdf")
          print("2)Accept the column names which the user wants to include in the  dataframe")
          print("3)Accept the number of rows reading from the top of csv to create the dataframe")
          print("4)Write the updated dataframe into a new csv file named  studen1.csv")
          print("5)Exit")
          ch = int(input("Enter Choice: "))
          if ch == 1:
            path = input("Enter the csv file name with path: ")
            stdf= pd.read_csv(path)
            print(stdf)
            if ch == 2:
              path = input("Enter the csv file name with path: ")
              y = eval(input("Enther the column name you want to include in the dataframe:" ))
              stdf= pd.read_csv(path,usecols=y)
              print(stdf)
            if ch == 3:
              path = input("Enter the csv file name with path: ")
              n = eval(input("Enter the number of rows you want to read from the csv: "))
              stdf=pd.read_csv(path,nrows=n)
              print(stdf)
            if ch == 4:
                    path = input("Enter the csv file name with path for writing: ")
                    stdf.to_csv(path,index=False)
                    print(stdf)


    elif ch == 5:
        print("Exiting the program")  
    else:
        print("Invalid option, please retry")
