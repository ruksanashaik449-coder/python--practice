class PythonChatbot:

    def __init__(self):
        self.questions = {
            "what is python":
                "Python is a high-level programming language. "
                "It is used in web development, data science, AI and automation.",

            "what is a variable":
                "A variable is used to store a value in a program. "
                "Example: name = 'Ruksana'.",

            "what are data types":
                "Common Python data types are int, float, string, list, "
                "tuple, dictionary, set and boolean.",

            "what is a list":
                "A list is an ordered and changeable collection of items. "
                "Example: numbers = [1, 2, 3].",

            "what is a tuple":
                "A tuple is an ordered collection of items that cannot be "
                "changed after it is created. Example: values = (1, 2, 3).",

            "what is a dictionary":
                "A dictionary stores data in key-value pairs. "
                "Example: student = {'name': 'Ruksana', 'age': 19}.",

            "what is a function":
                "A function is a reusable block of code used to perform "
                "a particular task.",

            "what is a loop":
                "A loop is used to execute a block of code repeatedly. "
                "Python mainly has for and while loops.",

            "what is a class":
                "A class is a blueprint for creating objects in Python. "
                "It is used in object-oriented programming.",

            "what is an exception":
                "An exception is an error that occurs while a program is "
                "running. We can handle it using try and except.",

            "what is numpy":
                "NumPy is a Python library used for numerical calculations "
                "and working with arrays.",

            "what is pandas":
                "Pandas is a Python library used for data analysis and "
                "working with tables and DataFrames.",

            "what is a string":
                "A string is a sequence of characters written inside quotes. "
                "Example: name = 'Ruksana'.",

            "what is a set":
                "A set is an unordered collection of unique elements. "
                "Example: numbers = {1, 2, 3}.",

            "what is a boolean":
                "A boolean has two possible values: True and False.",

            "what is an integer":
                "An integer is a whole number without a decimal point. "
                "Example: age = 19.",

            "what is a float":
                "A float is a number that contains a decimal point. "
                "Example: price = 10.5.",

            "what is an operator":
                "An operator is a symbol used to perform an operation. "
                "Examples are +, -, *, / and ==.",

            "what is an if statement":
                "An if statement is used to execute code when a condition is True.",

            "what is elif":
                "elif means else if. It is used to check another condition "
                "when the previous condition is False.",

            "what is else":
                "The else statement runs when the previous conditions are False.",

            "what is a for loop":
                "A for loop repeats a block of code for each item in a sequence.",

            "what is a while loop":
                "A while loop repeats code as long as a condition is True.",

            "what is break":
                "The break statement stops a loop before it normally finishes.",

            "what is continue":
                "The continue statement skips the current iteration and "
                "moves to the next iteration.",

            "what is pass":
                "The pass statement does nothing. It is used as a placeholder.",

            "what is indexing":
                "Indexing is used to access an individual item from a list "
                "or string.",

            "what is slicing":
                "Slicing is used to get a part of a list or string.",

            "what is a module":
                "A module is a Python file containing reusable code such as "
                "functions, classes or variables.",

            "what is a package":
                "A package is a collection of Python modules stored together.",

            "what is pip":
                "pip is a tool used to install and manage Python packages.",

            "what is an argument":
                "An argument is a value passed to a function when it is called.",

            "what is a parameter":
                "A parameter is a variable in a function definition that "
                "receives a value when the function is called.",

            "what is return":
                "The return statement sends a value back from a function.",

            "what is recursion":
                "Recursion is a technique where a function calls itself.",

            "what is inheritance":
                "Inheritance allows one class to use the properties and "
                "methods of another class.",

            "what is polymorphism":
                "Polymorphism allows the same operation to behave differently "
                "for different objects.",

            "what is encapsulation":
                "Encapsulation means keeping data and methods together inside "
                "a class and controlling access to them.",

            "what is abstraction":
                "Abstraction means hiding unnecessary details and showing "
                "only the important features.",

            "what is an object":
                "An object is an instance of a class. It contains data and "
                "can use the methods of its class.",

            "what is exception handling":
                "Exception handling is used to handle errors during program "
                "execution using try and except.",

            "what is a comment":
                "A comment is text written in code to explain the program. "
                "Python does not execute comments."
        }

    def find_answer(self, question):

        question = question.lower()
        question = question.strip()
        question = question.replace("?", "")

        if question in self.questions:
            answer = self.questions[question]
            return answer

        ignored_words = [
            "what", "is", "are", "a", "an", "the",
            "tell", "me", "about", "please", "explain"
        ]

        words = question.split()

        useful_words = []

        for word in words:
            if word not in ignored_words:
                useful_words.append(word)

        best_question = None
        highest_score = 0

        for stored_question in self.questions:
            stored_words = stored_question.split()
            score = 0

            for word in useful_words:
                if word in stored_words:
                    score = score + 1

            if score > highest_score:
                highest_score = score
                best_question = stored_question

        if best_question is not None and highest_score > 0:
            return self.questions[best_question]

        return "Sorry, I don't know the answer to that question yet."

    def chat(self):

        print("------------------------------------")
        print("          PYTHON CHATBOT")
        print("------------------------------------")
        print("Ask me a Python question.")
        print("Type 'exit' to stop the chatbot.")
        print()

        while True:

            question = input("You: ")

            if question.lower().strip() == "exit":
                print("Bot: Goodbye! Keep learning Python.")
                break

            answer = self.find_answer(question)

            print("Bot:", answer)
            print()


def main():

    chatbot = PythonChatbot()
    chatbot.chat()


if __name__ == "__main__":
    main()