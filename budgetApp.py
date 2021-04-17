# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 22:05:12 2021

@author: JENI
"""

class Budget:
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount
        
        
    def operations(self):
        print('Welcome!')
        print('''1. Withdrawal.
              2. Deposit.
              3. Transfers.
              4. check balance.
              ''')
        option = int(input('Enter your preferred option: \n'))
        if option == 1:
            self.withdrawal()
            
        elif option == 2:
            self.deposit()
            
        elif option == 3:
            self.transfer()
        elif option == 4:
            self.checkBal()
        else:
            print('Please enter avalid option from 1-4!')
            self.operations()
    
        
        
    def withdrawal(self):
        amountToWith = int(input('Enter amount you withdraw:\n'))
        if amountToWith > self.amount:
            print('Insufficient balance')
            self.anotherTrans()
        else:
            print(f'you have withdrawn {amountToWith} from your {self.category} balance')
            self.anotherTrans()
            
            
            
    def deposit(self):
        amountToDep =int( input('Enter the amount you wold to deposit: \n'))
        print(f'You have deposited the sum of {amountToDep} and your new balance is {amountToDep + self.amount}')
        self.anotherTrans()
        
        
    def transfer(self):
        amountToTrans = int(input('Enter amount to transfer: \n'))
        category = input('Enter category to transfer to: \n')
        if category == 'food':
            self.amount -=amountToTrans
            print(f'You have transferred {amountToTrans} to {category} account from {self.category} account') 
            self.anotherTrans()
            
        elif category == 'clothing':
            self.amount -=amountToTrans
            print(f'You have transferred {amountToTrans} to {category} account from {self.category} account')
            self.anotherTrans()
            
        elif category == 'entertainment':
            self.amount -=amountToTrans
            print(f'You have transferred {amountToTrans} to {category} account from {self.category} account')
            self.anotherTrans()
            
        else:
            print('Enter a valid category!')
            self.transfer()
            
            
    def checkBal(self):
        print(self.amount)
        self.anotherTrans()
        
    def anotherTrans(self):
        anotherTran = input('Would you like to perform another transaction? \n')
        if anotherTran == 'yes':
            self.operations()
        elif anotherTran == 'no':
            exit()
        else:
            print("Enter 'yes' or 'no'" )
            self.anotherTrans()
        
        
        
        
        
category_food = Budget('Food', 1000) 
category_clothing = Budget('clothing', 2000) 
category_entertainment = Budget('entertainment', 3000) 



   
        

        