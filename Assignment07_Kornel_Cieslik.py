# ------------------------------------------------------------------------------------------ #
# Title: Assignment07
# Desc: This assignment demonstrates using data classes
# with structured error handling
# Change Log: (Who, When, What)
#  Kornel Cieslik, 11/23/24, Created Script
# ------------------------------------------------------------------------------------------ #

import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''

FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
students: list = []  # a table of student data
menu_choice: str  # Hold the choice made by the user.


# Creation of the person class
class Person:
    """
    Represents a person with a first and last name.

    Attributes:
        first_name (str): The first name of the person.
        last_name (str): The last name of the person.
    """
    first_name: str = ''  # providing attribute first name
    last_name: str = ''  # providing attribute last name

    # creating a constructor and providing it with properties
    def __init__(self, first_name: str = "", last_name: str = ""):
        """
        Initializes a new instance of the Person class.

        Args:
            first_name (str): The first name of the person.
            last_name (str): The last name of the person.
        """
        self.first_name = first_name  # initializing first name
        self.last_name = last_name  # initializing last name

    @property  # creating the getter for the first name
    def first_name(self) -> str:
        """
        Gets the first name.

        Returns:
            str: The first name of the person.
        """
        return self.__first_name

    @first_name.setter  # creating the setter for the first name including validation code and dunderscores
    def first_name(self, value: str):
        """
        Sets the first name, ensuring it contains only letters.

        Args:
            value (str): The first name value.

        Raises:
            ValueError: If the value contains non-letter characters.
        """
        if value.isalpha():
            self.__first_name = value
        else:
            raise ValueError("First name should only contain letters")

    @property  # creating the getter for the last name
    def last_name(self) -> str:
        """
        Gets the last name.

        Returns:
            str: The last name of the person.
        """
        return self.__last_name

    @last_name.setter  # creating the setter for the last name including validation code and dunderscores
    def last_name(self, value: str):
        """
        Sets the last name, ensuring it contains only letters.

        Args:
            value (str): The last name value.

        Raises:
            ValueError: If the value contains non-letter characters.
        """
        if value.isalpha():
            self.__last_name = value
        else:
            raise ValueError("Last name should only contain letters")

    def __str__(self) -> str:  # overriding the __str__ method to produce a friendly readable string
        """
        Converts the person object to a user-friendly string.

        Returns:
            str: A formatted string with the person's details.
        """
        return f"Person(first_name='{self.first_name}', last_name='{self.last_name}')"


# creating a student class, defining it to inherit both attributes and properties
class Student(Person):
    """
    Represents a student enrolled in a course. Inherits from Person.

    Attributes:
        course_name (str): The name of the course the student is enrolled in.
    """

    # creating a constructor and providing it (3) properties
    def __init__(self, first_name: str, last_name: str, course_name: str = ""):
        """
        Initializes a new instance of the Student class.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            course_name (str): The name of the course.
        """
        super().__init__(first_name, last_name)  # pulling from the Person parent class
        self.course_name = course_name

    @property  # creating a getter for the course_name
    def course_name(self):
        """
        Gets the course name.

        Returns:
            str: The name of the course.
        """
        return self.__course_name

    @course_name.setter  # creating a setter with validation for the course name
    def course_name(self, value: str):
        """
        Sets the course name, ensuring it contains only letters, numbers, or spaces.

        Args:
            value (str): The course name value.

        Raises:
            ValueError: If the value contains invalid characters.
        """
        if value and all(x.isalnum() or x.isspace() for x in value):  # this checks for only letters, numbers,
            # or spaces for x in the value string
            self.__course_name = value
        else:
            raise ValueError("Course name should only contain letters, numbers, or spaces")

    def __str__(self) -> str:  # overwriting the __str__method to include course name in student data
        """
        Converts the student object to a user-friendly string.

        Returns:
            str: A formatted string with the student's details.
        """
        return f"Student(first_name='{self.first_name}', last_name='{self.last_name}', course_name='{self.course_name}')"

class FileProcessor:
    """Processing functions for file operations."""

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        try:
            with open(file_name, "r") as file:
                student_data = json.load(file)
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with reading the file.", error=e)
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        try:
            with open(file_name, "w") as file:
                json.dump(student_data, file)
            IO.output_student_and_course_names(student_data=student_data)
        except Exception as e:
            message = "Error: There was a problem with writing to the file.\n"
            message += "Please check that the file is not open by another program."
            IO.output_error_messages(message=message, error=e)


class IO:
    """Handles user input and output."""

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        print(menu)

    @staticmethod
    def input_menu_choice():
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1", "2", "3", "4"):
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())
        return choice

    @staticmethod
    def output_student_and_course_names(student_data: list):
        print("-" * 50)
        for student in student_data:
            print(f'Student {student["FirstName"]} {student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student = {"FirstName": student_first_name,
                       "LastName": student_last_name,
                       "CourseName": course_name}
            student_data.append(student)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages(message="Invalid input!", error=e)
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with your entered data.", error=e)
        return student_data


# Main loop
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

while True:
    IO.output_menu(menu=MENU)
    menu_choice = IO.input_menu_choice()

    if menu_choice == "1":
        students = IO.input_student_data(student_data=students)
    elif menu_choice == "2":
        IO.output_student_and_course_names(students)
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
    elif menu_choice == "4":
        break
    else:
        print("Please only choose option 1, 2, or 3.")

print("Program Ended")
