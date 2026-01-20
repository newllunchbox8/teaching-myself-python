passgrhigh = 99
passgrlow = 70
failgrlow = 1
failgrhigh = 69
perfectgr = 100
grade = int(input('enter your current grade without special characters: '))
if grade <= failgrhigh and grade >= failgrlow:
    print('you are failing your grade is ' + str(grade))
if grade <= failgrlow:
    print('jesus christ wtf is wrong with you your grade is ' + str(grade))
if grade >= passgrlow and grade <= passgrhigh:
    print('congrats you are passing your grade is ' + str(grade))
if grade > perfectgr:
    print('liar')
if grade == perfectgr:
    print('nerd')