a = int(input("Enter a :"))
b = int(input("Enter b :"))

try:
    result = a / b
except ZeroDivisionError:               # ZeroDivisionError    lihal nahi tari chalel.
    print("We not divide by zero.")
finally:
    print("The division is :",result)