# def main():
#     yell("This","Is","cs50")


# def yell(*words):
#     upper_case_words = []
#     for word in words:
#         upper_case_words.append(word.upper())

#     print(*upper_case_words)


# if __name__ == "__main__":
#     main()


# Now modifying using the map()

def main():
    yell("This","is","cs50","python")


def upper_string(word):
    return word.upper()
def yell(*words):
    upper_words = map(upper_string,words)
    print(*upper_words)


# if __name__ == "__main__":
#     main()


# List Comprehension

students = [
    {"name":"Harry Potter","house":"Gryffindorr"},
    {"name":"Draco Malfoy","house":"Slythrin"},
    {"name":"Harmioney Granger","house":"Gryffindorr"},
    {"name":"Neville Longbottom","house":"Gryffindorr"},
]

house_gryffindorr = [student["house"] for student in students if student["house"] == "Gryffindorr"]
# print(house_gryffindorr)


#  filters -> sort students based on their name of house gryffindorr

def is_gryffindorr(student):
    return student["house"] == "Gryffindorr"


house_gryffindorr_students = filter(is_gryffindorr,students)
# print("House Grffindorr...")
# for student in sorted(house_gryffindorr_students,key=lambda s:s["name"]):
#     print(student["name"])


# Dictinory Comprehension

student_list = ["Harry Potter","Ron Weasly","Nevill Longbottom","Harmioney Granger","Dean Thomas","Seamus Finnigen","Fred Weasly","George Weasly"]

student_hogwarts_house_list = [{"student name": student, "hogwarts house": "Gryffindorr"} for student in student_list]
# print(student_hogwarts_house_list)


studnts2 = ["harry","ron","harmioney","draco","neville"]

# for i,student in enumerate(studnts2):
#     print(f"Student Number: {i+1} Name: {student}")


#  Generators and Itterators

def main():
    number = int(input("Enter Number: "))
    for sheep in sheeps(number):
        print(sheep)


def sheeps(number):
    for _ in range(number):
        yield "🐑" * _


# if __name__ == "__main__":
#     main()


def positive_numbers(*numbers):
    for number in numbers:
        if number > 0:
            yield number


result = positive_numbers(1,-1,78,-895,25,-784,369,87,-895,-874,-785,14,-965)
# print(result)


for number in result:
    print(number)