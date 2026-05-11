def half(value):
    return value / 2 

# def double(value):
#     return value * 2 

def second(value):
    return value[1]

# double("22")
# print(double("22")) 
# 
# #I think it will return "2222", a string because you inputted a string. 
#I know it doesn't work at all times with different method but I guess if it is a string it will not cause an error


def double(number):
    return number * 3

print(double(10))

#The bug here can be in 2 different ways. It's either the number where the number will be multipled (3 = 2)
#Or the function name should be triple instead of double.

def open_account(balances, name, amount):
    balances[name] = amount

def sum_balances(accounts):
    total = 0
    for name, pence in accounts.items():
        print(f"{name} had balance {pence}")
        total += pence
    return total

def format_pence_as_string(total_pence):
    if total_pence < 100:
        return f"{total_pence}p"
    pounds = int(total_pence / 100)
    pence = total_pence % 100
    return f"£{pounds}.{pence:02d}"

balances = {
    "Sima": 700,
    "Linn": 545,
    "Georg": 831,
}

open_account(balances, "Tobi", 9.13)
open_account(balances, "Olya", "£7.13")

total_pence = sum_balances(balances)
total_string = format_pence_as_string(total_pence)

print(f"The bank accounts total {total_string}")










# class Person: 
#     def __init__(self, name: str, age: int, preferred_operating_system: str, address: str):
#         self.name = name
#         self.age = age
#         self.preferred_operating_system = preferred_operating_system
#         self.address = address

# imran = Person("Imran", 22, "Ubuntu", "Barcelona")
# print(imran.name)
# print(imran.address)  

# eliza = Person("Eliza", 34, "Arch Linux", "Barcelona")
# print(eliza.name)
# print(eliza.address)

# def is_adult(person: Person) -> bool:
#     return person.age >= 18

# print(is_adult(imran))

#Write a new function in the file that accepts a Person as a parameter and tries to access a property that doesn’t exist. Run it through mypy and check that it does report an error.
# def height(person: Person) -> None:
   
#     print(person.height)






# from dataclasses import dataclass
# from datetime import date

# @dataclass
# class Person:
#     name: str
#     date_of_birth: date
#     preferred_operating_system: str
#     address: str

#     def is_adult(self) -> bool:
#         today = date.today()
#         age = today.year - self.date_of_birth.year

#         # Adjust if birthday hasn't occurred yet this year
#         if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
#             age -= 1

#         return age >= 18

# imran = Person("Imran", date(2004, 5, 1), "Ubuntu", "Barcelona")
# eliza = Person("Eliza", date(1990, 3, 15), "Arch Linux", "Barcelona")

# print(imran.name)
# print(imran.address)
# print(imran.is_adult())

# print(eliza.name)
# print(eliza.address)
# print(eliza.is_adult())




# ✍️exercise
# Fix the above code so that it works. You must not change the print on line 17 - we do want to print the children’s ages. (Feel free to invent the ages of Imran’s children.)

# from dataclasses import dataclass
# from typing import List

# @dataclass(frozen=True)
# class Person:
#     name: str
#     age: int
#     children: List["Person"]

# fatma = Person(name="Fatma", age=12, children=[])
# aisha = Person(name="Aisha", age=9, children=[])

# imran = Person(name="Imran", age=31, children=[fatma, aisha])

# def print_family_tree(person: Person) -> None:
#     print(person.name)
#     for child in person.children:
#         print(f"- {child.name} ({child.age})")

# print_family_tree(imran)









# ✍️exercise
# Try changing the type annotation of Person.preferred_operating_system from str to List[str].

# Run mypy on the code.

# It tells us different places that our code is now wrong, because we’re passing values of the wrong type.

# We probably also want to rename our field - lists are plural. Rename the field to preferred_operating_systems.

# Run mypy again.

# Fix all of the places that mypy tells you need changing. Make sure the program works as you’d expect.



# from dataclasses import dataclass
# from typing import List

# @dataclass(frozen=True)
# class Person:
#     name: str
#     age: int
#     preferred_operating_systems: List[str]


# @dataclass(frozen=True)
# class Laptop:
#     id: int
#     manufacturer: str
#     model: str
#     screen_size_in_inches: float
#     operating_system: str


# def find_possible_laptops(laptops: List[Laptop], person: Person) -> List[Laptop]:
#     possible_laptops = []
#     for laptop in laptops:
#         if laptop.operating_system.lower() in (
#             os.lower() for os in person.preferred_operating_systems
#         ):
#             possible_laptops.append(laptop)
#     return possible_laptops


# people = [
#     Person(name="Imran", age=22, preferred_operating_systems=["Ubuntu"]),
#     Person(name="Eliza", age=34, preferred_operating_systems=["Arch Linux"]),
# ]

# laptops = [
#     Laptop(id=1, manufacturer="Dell", model="XPS", screen_size_in_inches=13, operating_system="Arch Linux"),
#     Laptop(id=2, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system="Ubuntu"),
#     Laptop(id=3, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system="ubuntu"),
#     Laptop(id=4, manufacturer="Apple", model="macBook", screen_size_in_inches=13, operating_system="macOS"),
# ]

# for person in people:
#     possible_laptops = find_possible_laptops(laptops, person)
#     print(f"Possible laptops for {person.name}: {possible_laptops}")




















# Write a program which:

# Already has a list of Laptops that a library has to lend out.
# Accepts user input to create a new Person - it should use the input function to read a person’s name, age, and preferred operating system.
# Tells the user how many laptops the library has that have that operating system.
# If there is an operating system that has more laptops available, tells the user that if they’re willing to accept that operating system they’re more likely to get a laptop.
# You should convert the age and preferred operating system input from the user into more constrained types as quickly as possible, and should output errors to stderr and terminate the program with a non-zero exit code if the user input bad values.

import sys
from dataclasses import dataclass
from enum import Enum


class OperatingSystem(Enum):
    MACOS = "macOS"
    ARCH = "Arch Linux"
    UBUNTU = "Ubuntu"


@dataclass(frozen=True)
class Person:
    name: str
    age: int
    preferred_operating_system: OperatingSystem


@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: OperatingSystem


laptops = [
    Laptop(1, "Dell", "XPS", 13, OperatingSystem.ARCH),
    Laptop(2, "Dell", "XPS", 15, OperatingSystem.UBUNTU),
    Laptop(3, "Dell", "XPS", 15, OperatingSystem.UBUNTU),
    Laptop(4, "Apple", "MacBook", 13, OperatingSystem.MACOS),
]


name = input("Name: ")

try:
    age = int(input("Age: "))
except ValueError:
    print("Age must be a number", file=sys.stderr)
    sys.exit(1)

os_input = input("Preferred operating system: ")

try:
    preferred_os = OperatingSystem(os_input)
except ValueError:
    print("Invalid operating system", file=sys.stderr)
    sys.exit(1)

person = Person(name, age, preferred_os)

matching_laptops = [
    laptop for laptop in laptops
    if laptop.operating_system == person.preferred_operating_system
]

print(f"There are {len(matching_laptops)} laptop(s) with {preferred_os.value}.")

best_os = preferred_os
best_count = len(matching_laptops)

for operating_system in OperatingSystem:
    count = len([
        laptop for laptop in laptops
        if laptop.operating_system == operating_system
    ])

    if count > best_count:
        best_os = operating_system
        best_count = count

if best_os != preferred_os:
    print(
        f"You are more likely to get a laptop if you accept "
        f"{best_os.value}, because there are {best_count} available."
    )