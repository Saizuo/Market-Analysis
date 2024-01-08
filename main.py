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
        print("4")
        # Additional code for option 4 can be added here
        
    elif ch == 5:
        print("Exiting the program")
        
        
    else:
        print("Invalid option, please retry")
