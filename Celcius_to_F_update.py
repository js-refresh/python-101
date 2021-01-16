while(True):
    try:
        C = float(input("What is temp in C?:  "))
        Fahrenheit = ((C*9/5)+32)
        print(f"You're temperature is {Fahrenheit} F")
        break
    except ValueError:
        print("That didn't work. Give me a number please.")
print('Thanks')






