import json
import random
import string
from pathlib import Path

class bank:
    database='data.json'
    data=[]
    try:
        if Path(database).exists():
            with open(database) as fs:
              data=json.loads(fs.read())
        else:
            print("no such file exists ")      
    except Exception as err:
        print(f'an error occured as {err}')
        
    @staticmethod
    def update():
        with open(bank.database,'w') as fs:
            fs.write(json.dumps(bank.data))
            
    @classmethod
    def _accountgenerate(cls):
        generate=random.randint(10000000,99999999)
        return generate    
            
            
                      
            
    def createaccount(self):
        info={
            'name':input('tell your name '),
            'age':int(input('Tell you age ')),
            'email':input('tell your email '),
            'pin':int(input(' write a 4 digit pin ')),
            'account number': bank._accountgenerate(),
            'balance':0
        }
        if info['age']<18 or len(str(info['pin'])) !=4:
            print('sorry you cannot create your account , possible causes \n: 1) pin must be of 4 digit\n  2) age must be 18 or above')
        else:
            print(' bank account created successfully ')
            print(f"👉 Your account number is: {info['account number']}")
            print(f"👉 Your balance is: {info['balance']}")
            
            
            bank.data.append(info)
            bank.update()
        
    def deposit(self):
        acc=int(input('please write your account number '))
               
        pin=int(input('please write your pin '))
              
        #search and verify account and update it
        for user in bank.data:
                if user['account number'] == acc and user['pin']==pin:
                    amt=int(input('enter the amount to deposit '))
                    user['balance']+=amt
                    print(f'{amt} deposited successfully \nUpdated balance= {user['balance']} INR')
                    bank.update()
                    return
                else:
                    print(' account not found or incorrent pin please try again :/')
    
    
    
    def withdraw(self):
        acc=int(input('please write your account number '))
               
        pin=int(input('please write your pin '))
        #search and verify account and update it
        for user in bank.data:
                if user['account number'] == acc and user['pin']==pin:
                    withdraw_amt=int(input('enter the amount to withdraw '))
                    if withdraw_amt > user['balance']:
                        print('INSUFFICENT BALANCE ...')
                    else:
                        user['balance']-=withdraw_amt
                        print(f'amount {withdraw_amt} INR  withdrawn successfully')
                        bank.update()
                        return    
    def details(self):
        acc=int(input('please write your account number '))
               
        pin=int(input('please write your pin '))
        #search and verify account and update it
        for user in bank.data:
                if user['account number'] == acc and user['pin']==pin:
                    print(f'account number : {user['account number']} \n name {user['name']} \n age is {user['age']} \n email is {user['email']}\n balance is {user['balance']}')
                else:
                    print("WRONG ACCOUNT NUMBER OR PIN ... TRY AGAIN :)")
                    
    def deleteaccount(self):
     acc = int(input("Enter your account number: "))
     pin = int(input("Enter your PIN: "))
     for account in bank.data:
        if account['account number'] == acc and account['pin'] == pin:
            bank.data.remove(account)  
            bank.update()
            print(" Account deleted successfully.")
            return
    print("❌ Invalid account number or PIN.")                  
                
print('press 1 for creating bank account')
print('press 2 for depositing')
print('press 3 for withdrawing monney ')
print('press 4 for details')
print('press 5 for deleting your account')

check =int(input('What is your response :- '))
user=bank()

if check==1:
    
    user.createaccount()
    
    
elif check==2:
    user.deposit()
    
elif check==3: 
    user.withdraw()   
    
elif check==4:
    user.details()   
    
else:
    check==5
    user.deleteaccount()