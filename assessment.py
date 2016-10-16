"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

Abstraction: In class we discussed abstraction as a way to hide details we don’t
need. To elaborate, it is a way to compartmentalize the attributes of a certain
object, or thing, in the abstract. For example, we could have an AbstractPlant
class that has properties that all plants have (roots, leaves, need for soil and
water, etc.).

This hides a lot of the details from the subclasses of particular plants -
Succulents, Trees, Houseplants - that we know share the same properties, and
allows these subclasses to inherit these properties without having to repeat
said properties in each subclass.

Thus we never have the need to call the AbstractPlant class directly, but we can
easily expand on what is inherited in the subclasses because of the information
in the AbstractPlant class.

Encapsulation: In class we discussed encapsulation as keeping everything
together. The way I understand it is organizational and functional in practice.

We can encapsulate a block of code into a function, or method, so that we can
use the result of the method in our program.

This makes our code much easier to read, but also prevents repetition and allows
simplicity.

Polymorphism: In class we discussed polymorphism as the interchangeability of
components.

This means that there could be a speak method in an abstract animal class, and
each subclass of animal also has a speak method.

However, the particular subclass, ex. Dog or Cat, responds differently when the
speak method is called. Ex, dog says “woof” and cat says “meow”.


2. What is a class?

A class is a “type” or thing, the way a string is a type str or an integer is a
type int.

3. What is an instance attribute? 

An instance attribute take a particular trait and can be called on a particular 
instance of an object.

In comparison to a class attribute, which shares the attribute with all
instances of the class (including subclasses), the instance attribute is only
applicable to that instance.


4. What is a method?

A method is the same a function defined, but defined in a class.


5. What is an instance in object orientation?

An instance is the individual occurrence of a class, aka an object. They are the same thing.


6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

   A class attribute is inherited from the base class by all subclasses. Use a
   class attribute on something that all instances share.

ex. In this case "nationality" is a class attribute that the subclass Tony inherits. 
self.name and self.position are instance attributes of the class object.


class SopranosCharacters(object):
    nationality = "italian"

    def __init__(self, name, position):
        "Initialize character attributes"

        self.name = name
        self.position = position

    def introduction(self):
        "Introduction of character"
        
        if self.position == "boss":
            print "This is Tony Soprano, the boss of the family."
        else: 
            print "This is one of Tony's soldiers,", self.name, "."

class Tony(SopranosCharacters):
    pass

"""

# Parts 2 through 5:
# Create your classes and class methods

class Student(object):
    """Student Class."""

    def __init__(self, first_name, last_name, address):
        """Student information."""

        self.first_name = first_name
        self.last_name = last_name
        self.address = address

class Question(object):
    """Question Class."""

    def __init__(self, question, correct_answer):
        """Question and correct answer initialization."""
        
        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        """Provides question and asks user for an input.

        Returns True if input matches correct answer.""" 

        ask_for_answer= raw_input(self.question + ": ")

        return ask_for_answer == self.correct_answer   


class Exam(object):
    """Exam Class."""

    def __init__(self, exam_name):
        """Initializing exam name and empty question list."""

        self.exam_name = exam_name
        self.questions = []

    def add_question(self, question, correct_answer):
        """Adds question and correspoinding answer to list."""
        
        new_question = Question(question, correct_answer)
        self.questions.append(new_question)

    def administer(self):
        """Administers exam and returns score."""

        score = 0

        for question in self.questions:

            if question.ask_and_evaluate() == True:
                score += 1

        return score

class Quiz(Exam):
    """Quiz Class, Subclass of Exam Class."""

    def administer(self):
        """Administers quiz and returns score."""

        result = super(Quiz, self).administer()
        num_of_questions = len(self.questions)

        return result >= (num_of_questions/2)

def take_test(exam, student):
    """Administers exam and returns student score."""

    exam_result = exam.administer()

    student.score = exam_result

    return student.score

def example(exam_name, first_name, last_name, address):
    """Example Exam, returns student score from administered exam."""

    midterm = Exam(exam_name)

    midterm.add_question("What color is the sky?", "blue")
    midterm.add_question("What color is the sky?", "blue")
    midterm.add_question("What color is the sky?", "blue")

    student_1 = Student(first_name, last_name, address)

    return take_test(midterm, student_1)




























