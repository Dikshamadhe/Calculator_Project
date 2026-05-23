#calculator project-1
''' 
so i want 1st 2 input from user then 
i want choice to ask for user like +,-,*,/,% 
use elif conditions

'''
Num_1 = float(input('Enter Number 1 :'))
Num_2 = float(input('Enter Number 2 :'))

# Asking user for operation choice
choice = input('Enter Your choice + , - ,* ,/ ,% , // ,** , ')

# Addition
if choice == "+":
   print(f'Addition: {Num_1 + Num_2}')

# Subtraction
elif choice == "-":
    print(f'Subtraction: {Num_1 - Num_2}')

# Multiplication
elif choice == "*":
    print(f'multiplication :{Num_1 * Num_2}')

# Division
elif choice == "/":
   print(f'divide :{Num_1 / Num_2}')

# Modulus
elif choice == "%":
   print(f'module :{Num_1 % Num_2}')

# Floor Division
elif choice == "//":
   print(f'floor division :{Num_1 // Num_2}')  #remove decimal


# Exponent / Power
elif choice == "**":
   print(f'exponsion :{Num_1 ** Num_2}')  #power

# Invalid input
else : 
    print('error!')
