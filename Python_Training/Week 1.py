import asyncio
import datetime

#Python Key Words

import asyncio


def menu():
    
    while True:
        print("\n" + "="*50)
        print("PYTHON LEARNING DEMOS")
        print("="*50)
        print("1. Python Keywords")
        print("2. Variables") 
        print("3. Statements & Comments")
        print("4. Type Conversions")
        print("5. Input/Output & Imports")
        print("6. DateTime & Algorithm Timing")
        print("7. Exit")
        
        choice = input("\nEnter your choice (1-7): ")
        
        if choice == "1":
            print("\n--- PYTHON KEYWORDS ---")
            key_words.key_words()
        elif choice == "2":
            print("\n--- VARIABLES ---")
            Variables.variables()
        elif choice == "3":
            print("\n--- STATEMENTS & COMMENTS ---")
            statements_comments.satements_somments()
        elif choice == "4":
            print("\n--- TYPE CONVERSIONS ---")
            Type_Conversions.Type_Conversions()
        elif choice == "5":
            print("\n--- INPUT/OUTPUT & IMPORTS ---")
            IO.IO()
        elif choice == "6":
            print("\n--- DATETIME & ALGORITHM TIMING ---")
            datetimee.datetimee()
        elif choice == "7":
            print("Thanks for learning Python! Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")
        
        # Pause before returning to menu
        input("\nPress Enter to return to the main menu...")


class key_words:
    def key_words():
        print("Let's learn some Python Key Words and Identifiers")
        user_in = input(
            "Choose from the following options: \n"
            " False\tawait\telse\timport\tpass \n"
            " None\tbreak\texcept\tin\traise \n"
            " True\tfinally\tis\treturn \n"
            " and\tcontinue\tfor\tlambda\ttry \n"
            " as\tfrom\twhile \n"
            " assert\tdel\tglobal\tnot \n"
            " async\telif\tif\tor\n"
        )
        user_in = user_in.lower()

        if user_in == "true" or user_in == "false":
            key_words.boolean()
        elif user_in == "async" or user_in == "await":
            asyncio.run(key_words.asyncawait())
        elif user_in in ("try", "except", "raise", "finally"):
            key_words.exceptionhandling()
        elif user_in == "assert":
            key_words.assertion()
        elif user_in == "global":
            key_words.globl()
        elif user_in in ("if", "elif", "else"):
            key_words.conditionals()
        elif user_in in ("for", "while", "break", "continue"):
            key_words.loops()
        elif user_in in ("import", "from", "as"):
            key_words.imports()
        elif user_in == "pass":
            key_words.passs()
        elif user_in == "none":
            key_words.nonee()
        elif user_in == "del":
            key_words.dell()
        elif user_in in ("is", "in", "not", "and", "or"):
            key_words.operators()
        else:
            print("Option not recognized. Please choose a valid keyword.")

    def boolean():
        TF = True
        while TF:
            print("TF is currently True")
            user_in = input("do you want the boolean variable TF to be True or False? ")
            user_in = user_in.lower()
            if user_in == "true":
                TF = True
            elif user_in == "false":
                TF = False
        print("TF is now False!")

    async def asyncawait():
        print("Asyncio is a Python library that allows for concurrent programming")
        print("Here is a mini program that displays two separate tasks running concurrently")

        async def arpits_meetings():
            meetings = [
                "6:00 AM meeting: 1",
                "6:30 AM meeting: 2",
                "7:00 AM meeting: 3",
                "7:30 AM meeting: 4",
                "8:00 AM meeting: 5",
                "8:30 AM meeting: 6",
                "9:00 AM meeting: 7",
                "9:30 AM meeting: 8",
            ]
            for meeting in meetings:
                print(f"Arpit’s {meeting}")
                await asyncio.sleep(1)

        async def dressing():
            items = ["shirt", "pants", "socks", "shoes"]
            for item in items:
                print(f"Putting on {item}")
                await asyncio.sleep(2)

        await asyncio.gather(
            arpits_meetings(),
            dressing()
        )
        print("Arpit is ready for work!")

    def globl():
        print("Lets learn how global works:")
        global counter
        counter = 0
        print(f"Initially, global counter = {counter}")

        def increment():
            global counter
            counter += 1
            print(f"Inside function, incremented counter to {counter}")

        increment()
        print(f"Back outside function, global counter is now {counter}")

    def exceptionhandling():
        print("The Try, Except, Raise and Finally blocks allow for developers to test blocks of code for errors and execute code how you want")
        print("we will now try to print x which is an unassigned variable: ")
        try:
            print(x)
            print("Because we used the try block, printing x, an unassigned variable, does not kill the program")
        except:
            print("An error was caused")
        finally:
            print("this demo is over (we use the finally block to print this regardless of any errors thrown)")

    def assertion():
        try:
            user_number = int(input("Input a number under 10 and I will verify it with assert: "))
            assert user_number < 10
            print("Good job, your number was less than 10")
        except:
            print("There has been an exception error")

    def conditionals():
        print("Conditional statements in Python: if, elif, else")
        num = int(input("Enter an integer: "))
        if num < 0:
            print("You entered a negative number.")
        elif num == 0:
            print("You entered zero.")
        else:
            print("You entered a positive number.")

    def loops():
        print("Python has the following loops: for, while, break, continue")
        print("\nExample of a for loop (printing 0 to 3):")
        for i in range(4):
            print(i)
        print("Example of a while loop (counting down from 3):")
        count = 3
        while count > 0:
            print(count)
            count -= 1
        print("break and continue in a for loop:")
        for j in range(1, 6):
            if j == 3:
                print("We just hit 3 so we use continue to skip it")
                continue
            if j == 5:
                print("We just hit 5, using break to exit loop.")
                break
            print(j)

    def imports():
        print("Importing modules:")
        print("Use 'import module_name' to bring in a module.")
        print("Use 'from module import name' to import specific items.")
        print("Use 'as' to give a module or object an alias, like:")
        print("  import math as m")

    def passs():
        print("The 'pass' statement does nothing; it’s just a placeholder.")
        print("Example in a loop:")
        for i in range(3):
            if i == 1:
                pass
            print(f"Loop iteration: {i}")

    def nonee():
        print("None means 'no value'.")
        var = None
        if var is None:
            print("var is currently None")
        var = 10
        print("Now var is:", var)

    def dell():
        print("The 'del' statement deletes a variable or element:")
        my_list = [1, 2, 3]
        print("Original list:", my_list)
        del my_list[1]
        print("After del my_list[1]:", my_list)

    def operators():
        print("This is going to demonstrate is, in, not in, and and")
        nums = [1, 2, 3]
        print("nums =", nums)
        print("Is 1 in nums? ", 1 in nums)
        print("Is 4 not in nums? ", 4 not in nums)
        print("Is (1 in nums) and (2 in nums)? ", (1 in nums) and (2 in nums))
        print("Is nums is nums? ", nums is nums)
        print("Is 1 is 1? ", 1 is 1)

class Variables:

    def variables():
        print ("Let's learn some Python Variables")
        x = "Give me a number to assign to x: "
        y = "Now give me a name to assign to y: "
        print(f"You're name is (y) {y} and you are (x) {x} years old")

class statements_comments:
    def satements_somments():
        print("Comments in python begin with a # \n You can also do multiline comments with '''")


class Type_Conversions:
    def Type_Conversions():
        user_in = None
        while user_in != "end":
            print ("Let's learn about Type Conversions!")
            user_in = input("enter a number (enter end to terminate loop): ")
            print(f"Your number is currently a: {type(user_in)}, now I will convert it to a integer using int(user_in)")
            user_in = int(user_in)
            print(f"Your number is now a: {type(user_in)}")


class IO:
    def IO():
        print("Let's learn about I/O and Import")
        name = input("Type your name and press Enter: ")
        print(f"Hello, {name}!")
        text = "Sample text for file I/O"
        with open("sample.txt", "w") as f:
            f.write(text)
        print("Wrote 'sample.txt' with sample text.")
        print("You can import modules like this: import math, you can also create an alias by doing: import random as rand")


class datetimee:
    def datetimee():
        print("Let's take a look at the datetime library")
        now = datetime.datetime.now()
        print(f"The current date and time is {now}\n")

        # Use a fixed list of 10 numbers
        sample_list = [34, 7, 23, 32, 5, 62, 32, 2, 90, 12]
        print(f"Using list: {sample_list}\n")

        print("Now let's find how efficient an algorithm is with datetime. First, we'll do a merge sort.\n")

        # --- Merge Sort Implementation --- (fixed n log n time complexity)
        def merge_sort(lst):
            if len(lst) <= 1:
                return lst

            mid = len(lst) // 2
            left = merge_sort(lst[:mid])
            right = merge_sort(lst[mid:])

            output = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    output.append(left[i])
                    i += 1
                else:
                    output.append(right[j])
                    j += 1

            while i < len(left):
                output.append(left[i])
                i += 1
            while j < len(right):
                output.append(right[j])
                j += 1
            
            return output

        # Time the merge sort
        start_merge = datetime.datetime.now()
        sorted_merge = merge_sort(sample_list.copy())
        end_merge = datetime.datetime.now()
        duration_merge = end_merge - start_merge
        print(f"Merge sort result: {sorted_merge}")
        print(f"Merge sort took: {duration_merge}\n")

        print("Now let's do a quick sort and measure its time.\n")

        # -- Quick Sort Implementation -- (n log n time complexity, n^2 worst case)
        
        def quicksort(list):
            
            if len(list) <= 1:
                return list
            else:
                pivot = list.pop()
                higher = []
                lower = []

            for i in list:
                if i < pivot:
                    lower.append(i)
                else:
                    higher.append(i)
            return quicksort(lower) + [pivot] + quicksort(higher)

        # Time the quick sort
        start_quick = datetime.datetime.now()
        sorted_quick = quicksort(sample_list.copy())
        end_quick = datetime.datetime.now()
        duration_quick = end_quick - start_quick
        print(f"Quick sort result: {sorted_quick}")
        print(f"Quick sort took: {duration_quick} (hh:mm:ss.ffffff)\n")
        # As you can observe, quick sort is faster with smaller sets
        print("That's how you can use the datetime library to compare algorithm runtimes!")


menu()