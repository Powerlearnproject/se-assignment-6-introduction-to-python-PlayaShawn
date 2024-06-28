[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/WfNmjXUk)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=15285649&assignment_repo_type=AssignmentRepo)
# SE-Assignment-6
 Assignment: Introduction to Python
Instructions:
Answer the following questions based on your understanding of Python programming. Provide detailed explanations and examples where appropriate.

 Questions:

1. Python Basics:
   - What is Python, and what are some of its key features that make it popular among developers? Provide examples of use cases where Python is particularly effective.

       Python is a high-level, interpreted programming language known for its simplicity & readability created by Guido Van Rossum.

        Key Features
          -Interpreted Language:The code is executed line by line making debugging easier and quicker.
          -Easy to learn and use: Simple syntax that mimics natural language hence it is ideal for begginers.
          -Versatile and Powerful: Supports various programming paradigms (procedural, object-oriented, functional).
          -Contains Extensive Libraries and Frameworks like NumPy, Pandas, Matplotlib, Django, Flask, etc.
          -Third-Party Modules and Packages: Python’s package manager, pip allows third-party apps installation.
          -Community and Support: Python has a large and active community.

        Use Cases:
          1. Web Development 
             Building server-side web applications, APIs, and web services using frameworks like Django/Flask.Google uses python for its API's.
          2. Data Science and Machine Learning
             Data analysis, statistical modeling, machine learning, and deep learning.Spotify utilizes python for backend services and data analysis.
          3. Artificial Intelligence and Robotics
             AI research, computer vision, natural language processing, and robotics.
          4. Software Development
             Prototyping, application development, and testing.Dropbox uses python for both client-side and server-side development.
          5. Financial Technology (FinTech)
             Quantitative analysis, algorithmic trading, risk management.
         

2. Installing Python:
   - Describe the steps to install Python on your operating system (Windows, macOS, or Linux). Include how to verify the installation and set up a virtual environment.

       Installing Python on Windows:
          1. Download Python Installer
             Visit the python website: python.org.
             Download the installer (e.g., python-3.x.x.exe).
          2. Run the Installer 
             Locate the downloaded installer and run it.
             Check the box that says “Add Python to PATH.” and install.
          3. Verify Installation
             Open Command Prompt (cmd).
             Type python --version and press Enter.
          4. Install pip (if not included) pip3 --version.

        Setting up virtual environment
          -Install 'venv' (if not included)
          -Create a Virtual Environment:
             Open cmd nad navigate to project directory.
             Run this command to create the environment 
                'python3 -m venv myenv'
          -Activate the Virtual Environment
             'myenv\Scripts\activate'
          -Verify the Virtual Environment Activation
             Run the command 'python --version'
          -Deactivate the Virtual Environment by typing 
             'deactivate'


3. Python Syntax and Semantics:
   - Write a simple Python program that prints "Hello, World!" to the console. Explain the basic syntax elements used in the program.
     Program:
       >>> print("Hello, World!")
       Output: 'Hello, World!'
     Syntax elements:
       -'print()' Function: built-in function in Python that outputs the specified message to the console.
       -String Literal data type:The text "Hello, World!" is a string literal enclosed with double/single quotes.
       -Parentheses '()': The parentheses are used to enclose the arguments passed to the 'print()' function.

      
4. Data Types and Variables:
   - List and describe the basic data types in Python. Write a short script that demonstrates how to create and use variables of different data types.

    Basic Data Types in Python
       -Integer (int):Represents whole numbers without a fractional component i.e '12'

       -Float: Represents numbers with a fractional component/decimal point.

       -String (str):sequences of characters enclosed in quotes.
       -List (list): an ordered collection of items, which can be of mixed data types.
          '[1, 2, 3], ["apple", "banana"]'

       -Tuple (tuple): an ordered collection of items, similar to a list, but tuples are immutable.
          '(1, 2, 3), ("a", "b", "c")'

       -Dictionary (dict):a collection of key-value pairs, with unique keys. 
          '{"name": "Alice", "age": 30}, {"key": "value"}'.
      
       Script @ E:\se-assignment-6-introduction-to-python-PlayaShawn\Script.py
      

5. Control Structures:
   - Explain the use of conditional statements and loops in Python. Provide examples of an `if-else` statement and a `for` loop.
     
    Conditional statements in Python are used to execute a block of code based on whether a condition is true or false.
       The primary conditional statements are 'if', 'elif' (else-if), and 'else'.

    Loops are used to execute a block of code repeatedly as long as a condition is met. 
       The primary loops in Python are 'for' and 'while'.
    
    Examples: E:\se-assignment-6-introduction-to-python-PlayaShawn\StateLoops.py
   

6. Functions in Python:
   - What are functions in Python, and why are they useful? Write a Python function that takes two arguments and returns their sum. Include an example of how to call this function.
    
    Functions in python are reusable blocks of code that perform a specific task.They help in organizing and structuring code.

    Benefits of Using Functions:
       -Code Reusability
       -Modularity
       -Readability
       -Maintainability

    Python Function Program: E:\se-assignment-6-introduction-to-python-PlayaShawn\PyFunction.py

7. Lists and Dictionaries:
   - Describe the differences between lists and dictionaries in Python. Write a script that creates a list of numbers and a dictionary with some key-value pairs, then demonstrates basic operations on both.
    
    Differences between lists and dictionaries in python
       Lists:
          -Ordered: Elements in a list have a specific order and each can be accessed by its index.
          -Mutable: Elements in lists can be modified after their creation.
          -Indexing: Access elements by their position in the list.
          -Syntax: Defined using square brackets '[]'.
       
       Dictionaries:
          -Unordered: Elements in a dictionary are stored as key-value pairs without any specific order (dictionaries in python 3.0+ maintain insertion order).
          -Mutable: Dictionaries can be modified after their creation.-Key-Based Access: Access elements by their unique keys.
          -Syntax: Defined using curly braces '{}' with key-value pairs separated by colons ':'.

    Lists and dictionaries script: [text](ListDict.py)


8. Exception Handling:
   - What is exception handling in Python? Provide an example of how to use `try`, `except`, and `finally` blocks to handle errors in a Python script.
    
    Exception handling in python is a mechanism used to handle runtime errors, allowing the program to continue executing or terminate. This is achieved using the:
       -'try'- Contains the code that might raise an exception.
       -'except'- Contains the code that runs if an exception occurs in the try block.
       -'finally'- Contains the code that runs no matter what, whether an exception occurs or not.

    Error handling python script: [text](Exception_Script.py)

9. Modules and Packages:
   - Explain the concepts of modules and packages in Python. How can you import and use a module in your script? Provide an example using the `math` module.
    
    Modules
       A module in python is a file containing python code that can define functions, classes, and variables(can also include runnable code).Help in organizing and structuring code into manageable parts.

    Packages
       A package is a collection of modules grouped together in a directory hierarchy. They allow for a hierarchical structuring of the module namespace using dot notation.

     Importing and Using Modules:
       You can import an entire module, specific functions, or classes from a module.
          
          Importing the math Module:
           'import math'
           # Using a function from the math module
            result = math.sqrt(16)
            print(f"The square root of 16 is {result}")

          Example script using math module: Module_import.py


10. File I/O:
    - How do you read from and write to files in Python? Write a script that reads the content of a file and prints it to the console, and another script that writes a list of strings to a file.
     
     Reading from and Writing to Files in Python
       In Python, you can use the built-in 'open()' function to work with files. 
       You can specify the mode in which the file should be opened such as read ('r'), write ('w'), append ('a'), etc.

    Script to Read from a File: [text](Script_To_Read.py)
    Script to Write a List of Strings to a File: [text](Script_To_Write.py)

# Submission Guidelines:
- Your answers should be well-structured, concise, and to the point.
- Provide code snippets or complete scripts where applicable.
- Cite any references or sources you use in your answers.
- Submit your completed assignment by [due date].


