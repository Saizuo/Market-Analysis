import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate
while True:
    username=input("Enter User Name : ")
    password=input("\nEnter Password : ")
    if username == "deepak" and password== "sharma":
        print("\nWelcome to EMPLOYEES MANAGEMENT SYSTEM\n")
        break
    else:
        print("Invalid Username or Password")

while True:
    print('\t\t *** Employees Data Analysis Project *** ')
    print('\n\t\t\t1. Data Analysis')
    print('\n\t\t\t2. Data Visualization')
    print('\n\t\t\t3. Data Operations')
    print('\n\t\t\t4. Exit\n')
   
    choice=int(input('Select your Choice [1-4] : '))

    if  choice==1:
              while True:
                    print('\t*** EMPLOYEES MANAGEMENT SYSTEM ***\n')
                    print('*'*50)
                    print("\n\t\t1. Show Employees Data")
                    print("\n\t\t2. Show Data Name-Wise")
                    print('\n\t\t3. Show first nth records')
                    print("\n\t\t4. Show last nth records")
                    print("\n\t\t5. Display employee with highest Salary")
                    print('\n\t\t6. Display employee with lowest Salary')
                    print("\n\t\t7. For Exit the program\n\n")
                    choice = int(input("Enter Your Choice [1-8] : "))
                    if choice == 1:
                        print("\nEmployees Data :\n\n")
                        df=pd.read_csv('D:\\Deepak\\2023-24\\XII IP\\Projects IP\\aastha_employees.csv')
                        print(tabulate(df,showindex=False,headers=['EMPNO','NAME','GENDER','BASIC','DA','HRA','CCA','PF','TOTAL','NET'],tablefmt='pretty'))
                    elif choice == 2:
                        print("\nEmployees Data Name - Wise :\n\n")
                        df=pd.read_csv('D:\\Deepak\\2023-24\\XII IP\\Projects IP\\aastha_employees.csv',usecols = ['NAME','GENDER','BASIC','DA','HRA','CCA','PF','TOTAL','NET'])
                        df = df.sort_values(by='NAME')
                        print(tabulate(df,showindex=False,headers=['NAME','GENDER','BASIC','DA','HRA','CCA','PF','TOTAL','NET'],tablefmt='pretty'))               
                    elif choice == 3:
                        print("\nFirst N Rows \n\n")                        
                        df=pd.read_csv('D:\\Deepak\\2023-24\\XII IP\\Projects IP\\aastha_employees.csv')
                        df = df.sort_values(by='EMPNO')                        
                        nth = int(input("How many rows to display? : "))                            
                        print(tabulate(df.head(nth),showindex=False,headers=['EMPNO','NAME','GENDER','BASIC','DA','HRA','CCA','PF','TOTAL','NET'],tablefmt='pretty'))
                    elif choice == 4:
                        print("\nLast N Rows \n\n")                        
                        df=pd.read_csv('D:\\Deepak\\2023-24\\XII IP\\Projects IP\\aastha_employees.csv')
                        df = df.sort_values(by='EMPNO')                        
                        nth = int(input("How many rows to display? : "))                            
                        print(tabulate(df.tail(nth),showindex=False,headers=['EMPNO','NAME','GENDER','BASIC','DA','HRA','CCA','PF','TOTAL','NET'],tablefmt='pretty'))
                    elif choice == 5:
                        print("\nDisplay employee with highest Salary :\n\n")                        
                        df=pd.read_csv('D:\\Deepak\\2023-24\\XII IP\\Projects IP\\aastha_employees.csv')
                        df = df.sort_values(by='NET')                        
                        print(tabulate(df.tail(1),showindex=False,headers=['EMPNO','NAME','GENDER','BASIC','DA','HRA','CCA','PF','TOTAL','NET'],tablefmt='pretty'))
                    elif choice==6:
                        print("\nDisplay employee with highest Salary :\n\n")                        
                        df=pd.read_csv('D:\\Deepak\\2023-24\\XII IP\\Projects IP\\aastha_employees.csv')
                        df = df.sort_values(by='NET')                        
                        print(tabulate(df.head(1),showindex=False,headers=['EMPNO','NAME','GENDER','BASIC','DA','HRA','CCA','PF','TOTAL','NET'],tablefmt='pretty'))
                    elif choice==7:
                       break
                    else:
                       print('Invalid Choice, Retry 1/2/3/4/5/6/7')                            
    elif choice==2:
              while True:
                print('Data Visualization')
                print('\n\t1. Plot Line Chart (Name and Basic Salary)')
                print('\n\t2. Plot Bar Chart  Vertical(Name and Basic Salary)')
                print('\n\t3. Plot Bar Horizontal Chart  (Name and Basic Salary)')
                print('\n\t4. Plot Histogram (Basic Salary)')
                print('\n\t5. Exit\n')              
                choic=int(input('Select your Choice [1-4] : '))

                if  choic==1:
                          print('Line Chart')
                          df=pd.read_csv('D:\\Deepak\\2023-24\\XII IP\\Projects IP\\aastha_employees.csv')
                          df['NAME'] = ['JOHN','MOHAN','SOHAN','RADHA','GEETA','SIMRAN','PRIYA','SIMMI','PREM','ASHWIN']
                          NAME=df["NAME"]
                          BASIC=df["BASIC"]
                         
                          plt.ylabel("Basic Salary ----------->")
                          plt.xlabel("Name -------->")
                          
                          plt.title("*** Name and Basic Salary ***")
                          
                          plt.plot(NAME,BASIC, color='r')
                          plt.grid()
                          plt.savefig('emp_line.pdf')
                          plt.show()                         
                elif choic==2:
                          print('Bar Chart')
                          df=pd.read_csv('D:\\Deepak\\2023-24\\XII IP\\Projects IP\\aastha_employees.csv')
                          df['NAME'] = ['JOHN','MOHAN','SOHAN','RADHA','GEETA','SIMRAN','PRIYA','SIMMI','PREM','ASHWIN']
                          NAME=df["NAME"]
                          BASIC=df["BASIC"]
                         
                          plt.ylabel("BASIC")
                          
                          plt.title("*** Name and Basic Salary ***")
                          
                          plt.bar(NAME,BASIC, color='r')
                          plt.grid()
                          plt.savefig('emp_bar.pdf')
                          plt.show()
                elif choic==3:
                          print('Bar Chart')
                          df=pd.read_csv('D:\\Deepak\\2023-24\\XII IP\\Projects IP\\aastha_employees.csv')
                          df['NAME'] = ['JOHN','MOHAN','SOHAN','RADHA','GEETA','SIMRAN','PRIYA','SIMMI','PREM','ASHWIN']
                          NAME=df["NAME"]
                          BASIC=df["BASIC"]
                         
                          plt.xlabel("Basic Salary")
                          plt.title("Name and Basic Salary")
                          
                          plt.barh(NAME,BASIC, color='r')
                          plt.grid()
                          plt.savefig('emp_barh.pdf')
                          plt.show()
                
                elif choic==4:
                          print('Histogram')
                          df=pd.read_csv('D:\\Deepak\\2023-24\\XII IP\\Projects IP\\aastha_employees.csv')
                          df['NAME'] = ['JOHN','MOHAN','SOHAN','RADHA','GEETA','SIMRAN','PRIYA','SIMMI','PREM','ASHWIN']
                          NAME=df["NAME"]
                          BASIC=df["BASIC"]
                         
                          plt.title("Name and Basic Salary")
                          
                          plt.hist(BASIC, color='r')
                          plt.grid()
                          plt.savefig('emp_hist.pdf')
                          plt.show()
                         
                elif choic==5:
                          print('Exit from menu........')
                          break
                else:
                          print('Invalid choice')                    
    elif choice==3:
              while True:
                print('Data Operations')
                print('\n\t1. Add a row to Dataframe')
                print('\n\t2. Remove a row to Dataframe')
                print('\n\t3. Add a Column to Dataframe')
                print('\n\t4. Remove a Column to Dataframe')
                
                print('\n\t5. Exit\n')              
                choic=int(input('Select your Choice [1-5] : '))

                if  choic==1:
                       df=pd.read_csv('D:\\Deepak\\2023-24\\XII IP\\Projects IP\\aastha_employees.csv')
                       EMPNO = int(input('Employee No : '))
                       NAME= input('Employee Name  : ')
                       GENDER = input('Gender [M/F/T] : ')
                       BASIC= int(input('Basic Salary : '))
                       DA=.50*BASIC
                       HRA=.30*BASIC
                       CCA=.10*BASIC
                       PF=.12*BASIC
                       TOTAL=BASIC + DA + CCA + PF
                       NET = TOTAL - PF
                       
                       cr=df['EMPNO'].count()
                       df1=pd.DataFrame({"EMPNO":EMPNO,"NAME":NAME,"GENDER":GENDER,"BASIC":BASIC,"DA":DA,"HRA":HRA,\
                                         "CCA":CCA,"PF":PF,"TOTAL":TOTAL,"NET":NET},index=[cr])
                       df=df.append(df1)
                       print(tabulate(df,showindex=False,headers=['EMPNO','NAME','GENDER','BASIC','DA','HRA','CCA','PF','TOTAL','NET'],tablefmt='pretty'))
                       print('Record added Successfully..............')
                    
                elif choic==2:
                     df=pd.read_csv('D:\\Deepak\\2023-24\\XII IP\\Projects IP\\aastha_employees.csv')                               
                     r=int(input("Enter the Employee Number to be removed : "))
                     df= df.drop(r-1)
                     print(tabulate(df,showindex=False,headers=['EMPNO','NAME','GENDER','BASIC','DA','HRA','CCA','PF','TOTAL','NET'],tablefmt='pretty'))
                     print('Record deleted Successfully..............')
                    
                elif choic==3:
                    print('Add a Column')
                    df=pd.read_csv('D:\\Deepak\\2023-24\\XII IP\\Projects IP\\aastha_employees.csv')                               
                    print("Add Column DEPARTMENT : ")
            
                    df['DEPARTMENT']=['HR','SALES','FINANCE','HR','SALES','FINANCE','HR','SALES','FINANCE','SALES']
                    print(tabulate(df,headers=['EMPNO','NAME','GENDER','BASIC','DA','HRA','CCA','PF','TOTAL','NET','DEPARTMENT'],tablefmt='pretty'))                
                    print('Column added Successfully..............')
                    
                elif choic==4:
                        print('Remove a Column')
                        df=pd.read_csv('D:\\Deepak\\2023-24\\XII IP\\Projects IP\\aastha_employees.csv')                               
                        C=input("Enter the Column Name to remove : ")
                        C=C.upper()
                        df=df.drop(C,axis=1)
                        print(tabulate(df,tablefmt='pretty'))                
                        print('Column removed Successfully..............')
                                         
                elif choic==5:
                          print('Exit from menu........')
                          break
                else:
                          print('Invalid choice')       
    elif choice==4:
              print('Exit from menu........')
              break
    else:
              print('Invalid choice')

 