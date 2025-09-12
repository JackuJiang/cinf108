
# assignment_part1.py
# -----------------------------------------------------------
#  Part 1 – 10 short exercises
#  Each exercise is isolated in its own section.
#  Run the file and follow the on-screen prompts.
# -----------------------------------------------------------

print("=== Part 1 – Ten quick exercises ===\n")

# -----------------------------------------------------------
# 1. Area of a rectangle
# -----------------------------------------------------------
def exercise_1():
    print("1. Area of a rectangle")
    try:
        length = float(input("   Enter length: "))
        width  = float(input("   Enter width : "))
        area   = length * width
        print(f"   Area = {area:.2f}\n")
    except ValueError:
        print("   Invalid input – skipping.\n")
exercise_1()

# -----------------------------------------------------------
# 2. Greeting with name and age
# -----------------------------------------------------------
def exercise_2():
    print("2. Greeting message")
    name = input("   Enter your name: ").strip()
    age  = input("   Enter your age : ").strip()
    print(f"   Hello {name}! You are {age} years old.\n")
exercise_2()

# -----------------------------------------------------------
# 3. Even or odd
# -----------------------------------------------------------
def exercise_3():
    print("3. Even or odd checker")
    try:
        n = int(input("   Enter an integer: "))
        print(f"   {n} is {'even' if n % 2 == 0 else 'odd'}.\n")
    except ValueError:
        print("   Not an integer – skipping.\n")
exercise_3()

# -----------------------------------------------------------
# 4. Max and min of a list
# -----------------------------------------------------------
# 4. 用户自己输入列表，然后找出最大/最小值
def exercise_4():
    print("4. Max & min of a list")
    raw = input("   Enter numbers separated by space: ").strip()
    if not raw:
        print("   No input – skipping.\n")
        return
    try:
        nums = [float(x) for x in raw.split()]
    except ValueError:
        print("   Invalid number detected – skipping.\n")
        return
    print(f"   Your list: {nums}")
    print(f"   Max = {max(nums)}, Min = {min(nums)}\n")
exercise_4()

# -----------------------------------------------------------
# 5. Palindrome check
# -----------------------------------------------------------
def is_palindrome(s: str) -> bool:
    s = str(s).lower()
    return s == s[::-1]

def exercise_5():
    print("5. Palindrome checker")
    txt = input("   Enter a string: ")
    print(f"   '{txt}' is {'a palindrome' if is_palindrome(txt) else 'not a palindrome'}.\n")
exercise_5()

# -----------------------------------------------------------
# 6. Compound interest
# -----------------------------------------------------------
def compound_interest(p, r, t, n=12):
    # p = principal, r = annual rate (as decimal), t = years, n = compounds per year
    return p * (1 + r/n)**(n*t)

def exercise_6():
    print("6. Compound interest calculator")
    try:
        p = float(input("   Principal amount: "))
        r = float(input("   Annual interest rate (%): ")) / 100
        t = float(input("   Time (years): "))
        print(f"   Amount after {t} years = { p * (r+1)**t}\n")
    except ValueError:
        print("   Invalid input – skipping.\n")
exercise_6()

# -----------------------------------------------------------
# 7. Days → years, weeks, days
# -----------------------------------------------------------
def exercise_7():
    print("7. Convert days to years, weeks, days")
    try:
        total_days = int(input("   Enter number of days: "))
        years = total_days // 365
        rem   = total_days % 365
        weeks = rem // 7
        days  = rem % 7
        print(f"   {total_days} days = {years} year(s), {weeks} week(s), {days} day(s)\n")
    except ValueError:
        print("   Not an integer – skipping.\n")
exercise_7()

# -----------------------------------------------------------
# 8. Sum of all positive numbers in a list
# -----------------------------------------------------------

def exercise_8():
    print("8. Sum of positive numbers")
    raw = input("   Enter integers separated by space: ").strip()
    if not raw:
        print("   No input – skipping.\n")
        return
    try:
        nums = [int(x) for x in raw.split()]
    except ValueError:
        print("   Invalid integer detected – skipping.\n")
        return
    pos_sum = sum(n for n in nums if n > 0)
    print(f"   Your list: {nums}")
    print(f"   Sum of positive numbers = {pos_sum}\n")
exercise_8()

# -----------------------------------------------------------
# 9. Count words in a sentence
# -----------------------------------------------------------
def exercise_9():
    print("9. Word-counter")
    sentence = input("   Enter a sentence: ")
    words = sentence.strip().split()
    print(f"   Number of words: {len(words)}\n")
exercise_9()

# -----------------------------------------------------------
# 10. Swap two variables
# -----------------------------------------------------------
def exercise_10():
    print("10. Swap two variables")
    try:
        a = float(input("   Value for a: "))
        b = float(input("   Value for b: "))
        print(f"   Before swap: a = {a}, b = {b}")
        a, b = b, a
        print(f"   After  swap: a = {a}, b = {b}\n")
    except ValueError:
        print("   Invalid input – skipping.\n")
exercise_10()

print("=== All exercises complete ===")