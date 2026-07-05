# pydantic is used for data validation,parsing and data serialization.
# pydantic works hard to convert input data-type to defined data type.

# strict types

from pydantic import BaseModel,Field,EmailStr
from pydantic import StrictInt
from typing import Optional, Literal


# class User(BaseModel):
#     name:str
#     age:int
#
# user = User(name="Arpit Mishra",age=27)
# print(user)
#
#
# class Employee(BaseModel):
#     id:StrictInt
#     name:str
#     department:str
#
#
# employee = Employee(name="John Doe",id="123",department="HR")
# print(employee)


# fields in pydantic

class Employee(BaseModel):
    name:str = Field(...,min_length=3,max_length=20)
    age:int = Field(...,gt=18,lt=65)
    email:EmailStr = Field(...,description="Employee's email address")
    department:Optional[str] = None
    gender:Literal['Male','Female','other'] = Field(...,description="Employee's Gender")

employee = Employee(name="Arpit Mishra",age=27,email="arpit.mishra.out@gmail.com",department="HR",gender="Male")
# print(employee)



# Serialization using pydantic
employee_obj = employee.model_dump() # it will give dictionary from pydantic object
print(employee_obj)
print(employee_obj['name'])


# another serialization is model_dump_json()
employee_json = employee.model_dump_json()
print(employee_json)
