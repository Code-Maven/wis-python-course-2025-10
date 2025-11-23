day = "Sunday" # str
print(type(day))

hours = 7
print(type(hours))

grade = 7.0
print(type(grade))

# print(dir(day))

# dont' do this!!!
# int = True
# print(int)

grade = True
print(type(grade))

days = ["Sunday", "Monday", "Tuesday"]
print(type(days))
print(type(days).__name__)
print(len(days))
# days.

things = [3, 1.2, "hello"]

week_days = ("Sunday", "Monday", "Tuesday")
print(type(week_days))
print(type(week_days).__name__)
print(len(week_days))
# week_days.

grades = {
    "Jane": 100,
    "Joe": 98,
}
print(grades)
print(type(grades))
#grades.

grades = {
    "Jane": [100, 37, 100],
    "Joe": 98,
}


grades = {
    "Jane": {
        "assignments": [100, 37, 100],        
    },
    "Joe": {
        "assignments": [99, 97, 98],
        "final_grade": 98,
    }
}

vector = [1, 4, 5]

matrix = [
    [7, 8, 9],
    [4, 5, 6],
]
print(matrix[0])
print(matrix[0][1])
print(matrix)

person1 = {
    "name": "Joe",
    "grade": 98,
}

person2 = {
    "name": "Jane",
    "grade": 100,
}



people = [
    {
        "name": "Joe",
        "grade": 98,
    },
    {
        "name": "Jane",
        "grade": 100,
    }
]
print(people)
print("--------")
for person in people:
    #print(person)
    print(person["name"])

## dimensions, complex data structures

results = [2, 3, 4]
## json


colors = set(["blue", "yellow"])
print(type(colors))
#colors.

# command line
import sys
sys.argv  # list
import argparse


