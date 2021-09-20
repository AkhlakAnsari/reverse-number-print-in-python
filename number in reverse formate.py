#num,ber print out in reverse formate using while loop
number =int(input('ENTER THE NUMBER:'))
reversed_number = 0

while number != 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number //= 10

print("REVERSED NUMBER IS: " + str(reversed_number))
#thanks akhlakansari94@gmail.com