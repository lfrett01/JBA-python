"""
Simple bot that asks questions/gives a quiz
"""
# greet user
def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')

# asks user to input name
def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')


# calculates a users name from their input
def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")

# counts to any number the user inputs
def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1

# creates a multiple choice quiz for the user
def test():
    print("Let's test your programming knowledge.")
    print("""Why do we use methods?
    1. To repeat a statement multiple times.
    2. To decompose a program into several small subroutines.
    3. To determine the execution time of a program.
    4. To interrupt the execution of a program""")
    x = int(input())
    while x != 2:
        print("Please, try again.")
        x = int(input())
    print('Completed, have a nice day!')


def end():
    print('Congratulations, have a nice day!')


greet('B0T', '2020')  
remind_name()
guess_age()
count()
test()
end()
