name = input("What is your name? \n")
allowedUsers = ['Seyi', 'Mike','Love']
allowedPassword = ['passwordSeyi','passwordMike','passwordLove']

if(name in allowedUsers):
    password = input("Your password? \n")
    userId = allowedUsers.index(name)

if(password == allowedPassword[userId]):
    print('Welcome %s' % name)

    from datetime import datetime
    Logintime = datetime.now()

    print("Login time is %s" %Logintime)
    
    print('These are the available options:')
    print('1. Withdrawal')
    print('2. Cash Deposit')
    print('3. Complaint')

selectedOption = int(input('Please select an option:'))

if(selectedOption == 1):
    input('How much would you like to withdraw? \n')
    print('Take your cash')
elif(selectedOption == 2):
    input('How much would you like to deposit? \n')
    output('Current balance')
elif(selectedOption == 3):
    input('What issue will you like to report? \n')
    v                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ('Thank you for contacting us')

else:
    print('Invalid option selected, please try again')