# import sys
# import argparse
# DOC-Strings in python
# def add_numbers(num1:int,num2:int):
#     """
#         Method to add two numbers
#     """
#     return num1 + num2


# # result = add_numbers(25,19)
# # print(result)

# if len(sys.argv) == 1:
#     print("Meow")
# else:
#     print("Usage: meow")



# parser = argparse.ArgumentParser()

# parser.add_argument("--numbers",int)
# args = parser.parse_args()
# # print(args.numbers)

import sys
import argparse

# parse_obj = argparse.ArgumentParser()
# parse_obj.add_argument('num1',type=int,help="Number 1")
# parse_obj.add_argument('num2',type=int,help="Argument 2")

# args = parse_obj.parse_args()
# result = args.num1 + args.num2
# print(result)


# def number_of_times_to_hello():
#     parser_obj = argparse.ArgumentParser(description="Enter number to tell how many times say hello!!")
#     parser_obj.add_argument("number",type=int,help="Number")
#     args = parser_obj.parse_args()
    
#     for _ in range(args.number):
#         print("Hello World!!")


# number_of_times_to_hello()


def greet_friend():
    """
        Method to greet a friend
    """

    argobj = argparse.ArgumentParser()
    argobj.add_argument("friends",nargs='+',type=str,help="List of friends")
    args = argobj.parse_args()

    for friend in args.friends:
        print(f"It's been a long time my friend: {friend}")

# greet_friend()


# Unpacking

def total(galleons,sickles,knuts):
    return (galleons * 17 + sickles) * 29 + knuts


amount = [17,25,50]
coins = {"galleons":17,"sickles":25,"knuts":50}
# print(total(amount[0],amount[1],amount[2]))
# print(total(*amount),'Knuts')
# print(total(coins["galleons"],coins["sickles"],coins["knuts"]))
# print(total(**coins))


# args and kwargs

def f(*args,**kwargs):
    print(f"Arguments: {args}")
    print(f"Keyboard Arguments: {kwargs}")


# f(25,56,78,galleons=25,sickles=78,knuts=95)   