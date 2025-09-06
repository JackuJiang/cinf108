import math
import string

# Exercise 1: Given a list of numbers, find the sum and average.
def exercise_1():
    numbers = list(map(float, input("Enter a list of numbers separated by spaces: ").split()))
    total_sum = sum(numbers)
    average = total_sum / len(numbers)
    print(f"Sum: {total_sum}, Average: {average}")

# Exercise 2: Create a program that takes a temperature in Celsius and converts it to Kelvin.
def exercise_2():
    celsius = float(input("Enter temperature in Celsius: "))
    kelvin = celsius + 273.15
    print(f"Temperature in Kelvin: {kelvin}")

# Exercise 3: Implement a program that checks if a given string is a palindrome.
def exercise_3():
    string = input("Enter a string: ")
    cleaned_string = ''.join(char.lower() for char in string if char.isalnum())
    print(f"The string is {'a palindrome' if cleaned_string == cleaned_string[::-1] else 'not a palindrome'}")

# Exercise 4: Create a function to reverse a given string.
def exercise_4():
    string = input("Enter a string: ")
    reversed_string = string[::-1]
    print(f"Reversed string: {reversed_string}")

# Exercise 5: Given a list of names, concatenate them into a single string separated by spaces.
def exercise_5():
    names = input("Enter a list of names separated by spaces: ").split()
    concatenated_string = ' '.join(names)
    print(f"Concatenated string: {concatenated_string}")

# Exercise 6: Write a Python program to check if a given string is a pangram (contains all letters of the alphabet).
def exercise_6():
    input_string = input("Enter a string: ").lower()
    alphabet = set(string.ascii_lowercase)  # Correctly using string module
    string_set = set(char for char in input_string if char.isalpha())
    print(f"The string is {'a pangram' if alphabet.issubset(string_set) else 'not a pangram'}")
    
# Exercise 7: Calculate the area and circumference of a circle given its radius.
def exercise_7():
    radius = float(input("Enter the radius of the circle: "))
    if radius<=0:
        print("the circle not exit") 
        exit
    else:
        area = math.pi * (radius ** 2)
        circumference = 2 * math.pi * radius
        print(f"Area: {area}, Circumference: {circumference}")

# Exercise 8: Implement a program that converts a given number of minutes into hours and minutes.
def exercise_8():
    minutes = int(input("Enter the number of minutes: "))
    hours = minutes // 60
    remaining_minutes = minutes % 60
    print(f"{minutes} minutes is {hours} hours and {remaining_minutes} minutes")

# Exercise 9: Create a function to count the number of vowels in a given string.
def exercise_9():
    string = input("Enter a string: ").lower()
    vowels = "aeiou"
    count = sum(1 for char in string if char in vowels)
    print(f"Number of vowels: {count}")

# Exercise 10: Write a program to check if a number is prime.
def exercise_10():
    num = int(input("Enter a number: "))
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                print(f"{num} is not a prime number")
                break
        else:
            print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")

# Main function to run all exercises
def main():
    while True:
        print("\nChoose an exercise to run:")
        print("1. Sum and average of a list of numbers")
        print("2. Convert Celsius to Kelvin")
        print("3. Check if a string is a palindrome")
        print("4. Reverse a string")
        print("5. Concatenate a list of names")
        print("6. Check if a string is a pangram")
        print("7. Calculate area and circumference of a circle")
        print("8. Convert minutes to hours and minutes")
        print("9. Count the number of vowels in a string")
        print("10. Check if a number is prime")
        print("0. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            exercise_1()
        elif choice == '2':
            exercise_2()
        elif choice == '3':
            exercise_3()
        elif choice == '4':
            exercise_4()
        elif choice == '5':
            exercise_5()
        elif choice == '6':
            exercise_6()
        elif choice == '7':
            exercise_7()
        elif choice == '8':
            exercise_8()
        elif choice == '9':
            exercise_9()
        elif choice == '10':
            exercise_10()
        elif choice == '0':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()