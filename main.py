# 1. Check Python version
# python --version

# 2. Hello script
print("Hello, my name is Hassan Ali")


#-----------------------------### Syntax & Indentation ####-----------------------------
# 1. Fix indentation
for i in range(3):
    print('Indented loop', i)

# 2. Add comments
# Loop through numbers 0 to 2
for i in range(3):
    # Print current index
    print('Indented loop', i)
    
   
#------------------------------### Variables & Types ####-------------------------------------------    
# 1. User profile with typed summary
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in cm: "))
print(f"Name: {name} ({type(name)}), Age: {age} ({type(age)}), Height: {height} ({type(height)})")

# 2. Swap two variables without temp
a, b = 5, 10
a, b = b, a
print(f"Swapped: a = {a}, b = {b}")



#-------------------------------#### Casting & I/O ####-------------------------------------------------
# 1. Average of 3 numbers
nums = [float(input(f"Enter number {i+1}: ")) 
        for i in range(3)]
print("Average:", sum(nums)/3)

# 2. Convert minutes to hours & minutes
minutes = int(input("Enter total minutes: "))
hours = minutes // 60
mins = minutes % 60
print(f"{minutes} minutes = {hours} hours and {mins} minutes")


#----------------------------------### Operators ###--------------------------------------------
# 1. BMI Calculator
weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))
bmi = weight / (height ** 2)
print(f"Your BMI is {bmi:.2f}")

# 2. Simple Interest
P = float(input("Principal amount: "))
R = float(input("Rate of interest: "))
T = float(input("Time in years: "))
SI = (P * R * T) / 100
print(f"Simple Interest: {SI}")


#--------------------------------------### Strings ###-----------------------------------------------
# 1. Username builder
full_name = input("Enter your full name: ").strip().lower()
username = "".join(full_name.split())
print("Username:", username)

# 2. Vowel/consonant counter
text = input("Enter a string: ").lower()
vowels = 'aeiou'
v_count = sum(1 for c in text if c in vowels)
c_count = sum(1 for c in text if c.isalpha() and c not in vowels)
print(f"Vowels: {v_count}, Consonants: {c_count}")


#-------------------------------------### Conditionals ###----------------------------------------
# 1. Grade calculator
marks = int(input("Enter your marks: "))
if marks >= 90:
    grade = 'A'
elif marks >= 75:
    grade = 'B'
elif marks >= 60:
    grade = 'C'
else:
    grade = 'D'
print("Grade:", grade)

# 2. Password strength
pwd = input("Enter password: ")
if len(pwd) >= 8 and any(c.isdigit() for c in pwd) and any(c.isupper() for c in pwd):
    print("Strong Password")
else:
    print("Weak Password")


#---------------------------------- ### Loops ###---------------------------------------
# 1. Multiplication table
num = int(input("Enter number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")

# 2. Sum numbers divisible by 3
n = int(input("Enter limit: "))
total = sum(i for i in range(n+1) if i % 3 == 0)
print("Sum of numbers divisible by 3:", total)



#---------------------------------------### cli unit converter ###------------------------------ 
def length_converter():
    m = float(input("Enter meters: "))
    print(f"{m} m = {m * 3.281:.2f} ft")

def weight_converter():
    kg = float(input("Enter kilograms: "))
    print(f"{kg} kg = {kg * 2.205:.2f} lb")

def temp_converter():
    c = float(input("Enter Celsius: "))
    print(f"{c}°C = {(c * 9/5) + 32:.2f}°F")

while True:
    print("\nUnit Converter:\n1. Length\n2. Weight\n3. Temperature\n4. Exit")
    choice = input("Choose option: ")
    if choice == '1':
        length_converter()
    elif choice == '2':
        weight_converter()
    elif choice == '3':
        temp_converter()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")




