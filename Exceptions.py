try:
    age = input("How old are you? ")
    print("In 2032 you will be ", int(age) + 10)
    print(100/int(age))

except ValueError:
    print("Hey this is not a number")
except ZeroDivisionError:
    print("Cannot be divided by zero")
except:
    print("That is an error that I had not seen")
finally:
    print("This is what we do after all is done")