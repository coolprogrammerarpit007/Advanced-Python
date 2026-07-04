# Object-Oriented Programming provides reusability and scalability along with readability
# Encapsulation

class School:

    # these are class variables
    name = "Tagore Public School"
    address = "Vaishali Nagar, Jaipur Rajasthan"
    student_count = 0

    def __init__(self,name,class_standard,addmission_year,roll_number,sex):
        self.name = name
        self.class_standard = class_standard
        self.addmission_year = addmission_year
        self._roll_number = roll_number
        self.sex = sex


    @property
    def roll_number(self):
        return f"{self.name} is student  and  {'his' if self.sex == 'Male' else 'her' } roll number is: {self._roll_number}!"

    @roll_number.setter
    def roll_number(self,value):
        self._roll_number = value


    def student_introduction(self):
        return f"Student name is {self.name}, {'his' if self.sex == 'Male' else 'her' } roll number is {self._roll_number} and of class standard is {self.class_standard}"


    @classmethod
    def new_student_enrollment(cls,student_info):
        cls.student_count += 1
        name,class_standard,enrollment_year,roll_number,sex = student_info.values()
        new_student = cls(name,class_standard,enrollment_year,roll_number,sex)
        return new_student


# Template Dictionary Representation
student_dict = {
    "name": "John Doe",
    "class_standard": "10th Grade",
    "addmission_year": 2024,
    "_roll_number": 101,  # Protected attribute convention
    "sex": "Male",
}

student1 = School.new_student_enrollment(student_dict)

# student1 = School("Arpit","12th","2014-16","LWP1012","Male")

print(student1.name)




