# =======================================================================================================================================
# =======================================================     INDEX: HOW TO     =========================================================
# ======================================================================================================================================= 


        # 1 Hashtag are Comemnts/Analogies and Explanations
        ## 2 Hashtags are runable code, delete the hashtags to run the code/add or change the code for practice
        ### 3 Hashtags are partial codes that you can copy and paste into the runnable code to see diffrent outcomes
        #### 4 Are fun tasks for you to practice


        # NOTE To run the code below delete 2 ## hastags at the start of every line this will uncomment them. below will tell you how using shortcut:


        # 1. Highlight all the code with 2 ##
        # 2. Once highlight use shortcuts to uncomment to run the code:

                        # macOS: Cmd + /                # Do this 2 times as there is 2 ##
                        # Windows/Linux: Ctrl + /       # Do this 2 times as there is 2 ##
        
        # 3. Run the code to see the results in the terminal

        # Assuming you are using Vscode and you are using this file, you should see a play button on top right corner 
        # The outcome will appear in the terminal 
        # Option 2 is to run the file from the terminal this is done by typing
                                            
                # python3     then the name of the file, in this case it will be LearnPython.py
                # so in my case to run this file the command will be.
                                                        
                        # macOS:                python3 LearnPython.py
                        # Windows/Linux:        python LearnPython.py

        # Open A Terminal Using Keyboard Shortcuts
                # 1. Using Keyboard Shortcuts
                # Windows/Linux: Press Ctrl + (Backtick)
                # macOS: Press Cmd + (Backtick)
                # The backtick key () is usually located just above the Tab` key.

                # 2. Using the Top Menu
                # Go to the top menu bar:
                # Windows/Linux: View > Terminal
                # macOS: View > Terminal
                # This will open the integrated terminal at the bottom of your VSCode window.

        # NOTE Once you run the code and moving on to the next section put the comment ## back this will comment them again.
                        
        # 4. Highlight all the code you uncommented 
        # 5. Once highlight use shortcuts to omment to run the code:

                        # Windows/Linux: Ctrl + Z       # Do this 2 times as there is 2 ##
                        # macOS: Cmd + Z                # Do this 2 times as there is 2 ##


# =======================================================================================================================================
# ========================================================= 1. COMMUNICATION PRINT() ====================================================
# =======================================================================================================================================                                              

# Analogy:
# print() function is like a computers mouth, when you write print what ever is inbetween () the computer will say out load (print out)



## print ("Hello world")

                    # Results will be :  Hello world 

# NOTE To run this code above delete 2 ## hastags at the start of every line  this will uncomment them below will tell you how using shortcut:


                        # 1. Highlight all the code with 2 ##
                        # 2. Once highlight use shortcuts to uncomment to run the code:

                                        # macOS: Cmd + /                # Do this 2 times as there is 2 ##
                                        # Windows/Linux: Ctrl + /       # Do this 2 times as there is 2 ##

                        # 3. Look at the index at the top of this page for instruction on how to run the run and see results 
                        
                        # NOTE Once you run the code and moving on to the next section put the comment ## back this will comment them again.
                        
                        # 1. Highlight all the code you uncommented 
                        # 2. Once highlight use shortcuts to omment to run the code:

                                        # Windows/Linux: Ctrl + Z       # Do this 2 times as there is 2 ##
                                        # macOS: Cmd + Z                # Do this 2 times as there is 2 ##

#### TASK
    # Try it your self. Can you get the computer to say "I Love Coding" 🚀✨


# =======================================================================================================================================
# ========================================================= 2. VARIABLES  ===============================================================
# ======================================================================================================================================= 
                                                
# Variables - Your Storage Boxes
# In Python, variables are like labeled storage boxes where you can keep information.

# Analogy:
# Imagine you’re organizing a shelf:
# 	•	You label one box “Apples” and put 10 apples inside.
# 	•	Another box is labeled “Bananas” with 5 bananas.
            
                        # apples = 10
                        # bananas = 5

# Now the computer knows:
# 	•	apples holds 10.
# 	•	bananas holds 5.
# You can ask it to add them by using the print():



## apples = 10
## bananas = 5
## print (apples + bananas)

                        # Result will be : 15


#### TASK 
    # Do you think can test it out? 
    # What if i had 8 Oranges 3 Pineapples and 7 Avocados 
    # How would i get the resutls of the total number of fruit i have?
    # TRY IT 🚀✨

# =======================================================================================================================================
# ========================================================= 3. DATA TYPES  ==============================================================
# ======================================================================================================================================= 
                                               

# Not all boxes store the same type of thing! Python has different kinds of storage boxes:

# 	•	int: Numbers (like 5 or 10) → Think: A box for counting items.
# 	•	str: Text/Strings (like “Hello”) → Think: A box for letters or words.
# 	•	float: Decimal numbers (like 3.14) → Think: A box for precise measurements.
# 	•	bool: True/False → Think: A yes/no box.

                        # age = 39              # int
                        # name = "Will"         # str 
                        # price = 19.99         # float
                        # is_happy = True       # bool


# NOTE we will chat about these later. now lets have a look at input() fanction and what it does 


# =======================================================================================================================================
# ================================================== 4. INPUT() - LISTENNING TO YOU =====================================================
# ======================================================================================================================================= 
                                            
# input() function is how you make the computer ask questions. 

# Analogy:
# The computer is like a waiter asking, "whats your name" and “What do you want to order?”

## name = input("What's your name? ") # here we are telling the compueter to ask for your name
## print("Hello, " + name + "!") # here we are taking the results of the name adding Hello before the name and printing both Hello + name + "!"

# The input itself is your name something that the user put in (input)

# We are asking the computer to do 3 things 

                        # 1. ask for a name     
                        # 2. take the result and print Hello infront of it
                        # 3. and finally add "!" at the end    

                        # Results will be : What's your name? Will  (WILL IS MY INPUT AS AN ANSWER TO THE QUESTION)
                        #                   Hello, Will!


# =======================================================================================================================================
# ================================================= 4.1 INPUT PART 2 ADDING MENU ========================================================
# ======================================================================================================================================= 
                                        
# Lets build on what we have learned so far and add a menu 
                        
                        # 1. we want to welcome the user and ask for their name 
                        # 2. Once we have the users name we want to say Hello + Name + Give them the Menu 
                        # 3. Display the menu 
                        # 4. Take the users order via an input 
                        # 5. confirm the order by displaying a (messege + name + message + order + message) 

# In these functions we will be using (int) and (str)  

# So far we know how to Welocme users and ask for their name 

                        # name = input("Welcome to Python Diner! What's your name? ")
                        #                       str                     str

# But how would we show them a menu?
# The first part is the same as we done before we just add it to the print function
# We will add more text to the last str that will diplay "Here's our menu"

# NOTE we didn't add a new string(str) we added more text to the existing (str)  "!"

                        # print("Hello, " + name + "! Here's our menu:")

# Great we now  did a few cool things: 

                        # We welcomed the used
                        # We asked for thier Name
                        # We got their name 
                        # We said Hello (using their name)
                        # and we verbally gave them a menu

# But no menu is visible, so how do we create a menu they can see and intract with?

# To do this we use the print() function again 

                        # print("""
                        # Menu:
                        # 1. Pizza      #int
                        # 2. Burger     #int
                        # 3. Pasta      #int
                        # """)

# =======================================
# =========== SIDE QUEST 1 ==============
# =======================================

# What Are """ """?
# In Python, """ """ (triple quotes) are used to create multi-line strings.

# When Should You Use """ """?
# When creating a multi-line message or text (like our menu).
# Or
# When writing documentation or comments for your code. For example:

# when writing a comment its simply used like this 

"""
This function displays the menu for the Python Diner. 
"""

# When used in function is it inside ( ) so the computer Recognises its something that we want printed and not ignored like a comment

                        # print("""                             # What does this print() function do?
                        # Menu:                                 # This Function prints out Menu:
                        # 1. Pizza      #int                    # Option 1 (A Pizza)
                        # 2. Burger     #int                    # Option 2 (A burger)
                        # 3. Pasta      #int                    # Option 3 (A Pasta)
                        # """)                                  

# NOTE We are using numbers (int) to indentify the the food options. when the computer sees this it only sees numbers (int) not the name of the foods!
                        # The name of the food options are only visible to the user.


# Great our code so far should look like this:
                        # Step 1:  welcome the customer and Ask for the customer's name
                        # name = input("Welcome to Python Diner! What's your name? ") 

                        # #Step 2: Greet the customer with their name collected for the previous input() and display "Here's our menu"
                        # print("Hello, " + name + "! Here's our menu:")

                        # # Step 3: Display the menu
                        # print("""
                        # Menu:
                        # 1. Pizza      #int
                        # 2. Burger     #int
                        # 3. Pasta      #int
                        # """)


## #Step 1: Ask for the customer's name
## name = input("Welcome to Python Diner! What's your name? ") 

## #Step 2: Greet the customer
## print("Hello, " + name + "! Here's our menu:")

## # Step 3: Display the menu
## print("""
## Menu:
## 1. Pizza
## 2. Burger
## 3. Pasta
## """)

## # Step 4: Take the customer's order
## order = input("What would you like to order? (Type the name of the dish) ")

## # Step 5: Confirm the order
## print("Great choice, " + name + "! We'll prepare your " + order + " right away.") 

                    # Results will be:
                    # Welcome to Python Diner! What's your name? Will 
                    # Hello, will! Here's our menu:

                    # Menu:
                    # 1. Pizza
                    # 2. Burger
                    # 3. Pasta

                    # What would you like to order? (Type the name of the dish) 2
                    # Great choice, will! We'll prepare your 2 right away.
                        # (messege + name + message + order + message) 
                        #    str      str     str      int      str


# NOTE that we used Number (int) to indentify menu option the results show a Int (number) instead of the name of the item


# =======================================================================================================================================
# ============================================ 4.3 INPUT PART 3 USING STR TO REPLACE INT ================================================
# ======================================================================================================================================= 

# If we wanted for the results to show the name of the iteams instead of a number we would change the int (number) to a str (Text)
# We simply do this by modifying how the computer would read the iteams from numbers to text.            
            
                    # Step 3: Display the menu
                    ### print("""
                    ### Menu:
                    ### "Pizza"
                    ### "Burger"
                    ### "Pasta"
                    ### """)

# Try replacing step 3 in the runable code with this (str) Menu to see the diffrence  

# we would remove the numbers (int) and we would put the iteams in "" (string) 

                    # Results we now be diffrent istead of a int input (you putting in a number to choose what you want to eat)
                            # you will have to write what you what you want to eat e.g Pizza 
                            # the computer output will also say Pizza instead
                    # Welcome to Python Diner! What's your name? Will
                    # Hello, Will! Here's our menu:

                    # Menu:
                    # "Pizza"
                    # "Burger"
                    # "Pasta"

                    # What would you like to order? (Type the name of the dish) pizza
                    # Great choice, Will! We'll prepare your pizza right away.
                        #(messege + name + message + order + message) 
                        #   str      str     str      str     str
# NOTE


# =======================================================================================================================================
# ============================================= 5 DATA TYPES PART 2 DATA types  AT WORK ==================================================
# ======================================================================================================================================= 


#Individual Examples for Each Data Type:

                        # 1. Integer (int) Example:

## age = int(input("Enter your age: "))
## print("Your age in 5 years will be:", age + 5)

                        # 2. String (str) Example:

## name = input("Enter your name: ")
## print("Hello, " + name + "! Nice to meet you.")

                        # 3. Float Example:

## height = float(input("Enter your height in meters: "))
## print("Your height in centimeters is:", height * 100)

                        # 4. Boolean Example:

## is_happy = input("Are you happy today? (yes/no): ").strip().lower() == "yes"
## print("It’s great to hear you’re happy!" if is_happy else "Hope you feel better soon!")





                        # Combined Code for All Data Types:

## #Integer (int) Example
## age = int(input("Enter your age: "))
## print("Your age in 5 years will be:", age + 5)

## #String (str) Example
## name = input("Enter your name: ")
## print("Hello, " + name + "! Nice to meet you.")

## #Float Example
## height = float(input("Enter your height in meters: "))
## print("Your height in centimeters is:", height * 100)

## #Boolean Example
## is_happy = input("Are you happy today? (yes/no): ").strip().lower() == "yes"
## print("It’s great to hear you’re happy!" if is_happy else "Hope you feel better soon!")


                        # Enter your age: 39
                        # Your age in 5 years will be: 44
                        # Enter your name: Will
                        # Hello, Will! Nice to meet you.
                        # Enter your height in meters: 1.85
                        # Your height in centimeters is: 185.0
                        # Are you happy today? (yes/no): yes
                        # It’s great to hear you’re happy!
