'''
Pydantic is a data validation similart to springboot data validation
'''

from pydantic import BaseModel, field_validator, FieldValidationInfo, conint, Field
import datetime
from typing import Optional
from enum import Enum

class Level(Enum):
    BEGINNER = 1
    INTERMEDIATE = 2
    ADVANCED = 3

class Student (BaseModel) :
    first_name: str
    last_name: str
    alias: Optional[str] =  Field(default = None, validate_default=True)
    age: conint(ge=10, lt=30)
    date_joined: datetime.date
    level: Level
    password :Optional[str] 
    confirm_password :Optional[str]  

    # @field_validator("age")
    # def validate_age(cls, age):
    #     if (age <= 10):
    #         raise ValueError("Age must be above 10")
    #     return age
    
    @field_validator("level")
    def validate_level_from_age(cls, level, info:FieldValidationInfo):
        if level is Level.ADVANCED and info.data["age"] < 14 :
            raise ValueError("Age must be above 14 to be advanced level Student")
    
    @field_validator("alias")
    def validate_title(cls, val: Optional[str], info: FieldValidationInfo) -> str:
        if val is None:
            return info.data.get("first_name")
        return val

    @field_validator()
    def verify_password_match(cls,values):
        password = values.get("password")
        confirm_password = values.get("confirm_password")

        if password != confirm_password:
            raise ValueError("The two passwords did not match.")
        return values

student = Student(
    first_name="John",
    last_name="Oppenheimer",
    age=15,
    date_joined=datetime.date(2021,8,17),
    level=Level.ADVANCED
)

print(student)