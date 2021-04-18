Category = input("What categroy of the budget would you like to access? \n")
Allowed_Category = ['Food','Clothing','Entertainment']
if (Category in Allowed_Category):
    print ('Welcome to the %s Category' % Category)


Options = input("What do you want to do? \n")
Allowed_Options = ['Deposit','Withdraw','Compute Balance', 'Transfer between categories']
if (Options in Allowed_Options):
    print ('Welcome to the %s Section' % Options)

Starting_balance = [0,0,0]

class Budget:
        if (Options == 'Deposit'):
            def deposit_money(self):
                deposit_question = int(input("How much would you like to deposit in your" + self.deposit + " ? \n" ))
                print ("%d$ deposited in" % deposit_question + self.deposit)
        if (Options == 'Withdraw'):
            def withdraw_money(self):
                withdraw_question = int(input("How much would you like to withdraw from your" + self.withdraw + " ? \n" ))
                print("%d$ withdrawn from" % withdraw_question + self.withdraw)
        if (Options == 'Compute Balance'):
            def Balance_money(self):
                withdraw_question = input("What Category would you like to know the balance ? \n")
                print("withdraw_question")
Food = Budget()
Food.deposit = " Food Budget"
Food.withdraw = " Food Budget"

Clothing = Budget()
Clothing.deposit = " Clothing Budget"
Clothing.withdraw = " Food Budget"

Entertainment = Budget()
Entertainment.deposit = " Entertainment Budget"
Entertainment.withdraw = " Entertainment Budget"

if (Category == 'Food' and Options == 'Deposit'):
    Food.deposit_money()
   
if (Category == 'Food' and Options == 'Withdraw'):
    Food.withdraw_money()

if (Category== 'Clothing' and Options == 'Deposit'):
    Clothing.deposit_money()

if (Category== 'Clothing' and Options == 'Withdraw'):
    Clothing.withdraw_money()

if (Category== 'Entertainment' and Options == 'Deposit'):
    Entertainment.deposit_money()

if (Category== 'Entertainment' and Options == 'Withdraw'):
    Entertainment.withdraw_money() 
