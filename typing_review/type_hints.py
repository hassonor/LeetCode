from __future__ import annotations
from dataclasses import dataclass
from typing import (
    List,
    Set,
    Tuple,
    Dict,
    Union,
    Type,
    Optional,
    TypedDict,
    NamedTuple,
)

nums: List[int] = []
three_dimensional_vector: Tuple[int, float, str] = (1, 2.0, "Hey")
n_dimensional_vector: Tuple[float, ...] = 1, 2, 3, 4, 5
students_to_ages: Dict[str, int] = {
    "Or": 30,
    "Or2": 20,
}

fruits: Set[str] = {"Apply", "Kiwi", "Banana"}

miscellaneous_values: List[Union[int, float, str, Type]] = [
    1,
    "Hey",
    2.0,
    3,
    "Hello",
]

miscellaneous_values2: List[int | float | str | Type] = [
    1,
    "Hey",
    2.0,
    3,
    "Hello",
]

x: Union[int, float, str, Type]
y: int | float | str | Type
z: Optional[int] = None


def greet(name: Optional[str] = None):
    if not name:
        print("Hello")
        return
    print(f"Hello, {name}")


def greet2(name: str | None = None):
    if not name:
        print("Hello")
        return
    print(f"Hello, {name}")


# students: Dict[str, Union[str, int]] = {"name": "Marcy", "age": 25}


class Point(NamedTuple):
    x: int
    y: int


bob: Student

point2d = Point(1, 2)
print(point2d)
print(point2d.x)
print(point2d.y)


class Student(TypedDict):
    name: str
    age: int
    position: Point
    friends: List["Student"]


student: Student = {"name": "Marcy", "age": 25, "position": Point(1, 2), "friends": [
    {
        "name": "Jared",
        "age": 25,
        "position": Point(1, 2),
        "friends": []
    }
]}

student2 = Student(
    **{
        "name": "Marcy",
        "age": 27,
        "position": Point(1, 2),
        "friends": [
            Student(
                **{
                    "name": "Jared",
                    "age": 27,
                    "position": Point(1, 2),
                    "friends": []
                }
            )
        ]
    }
)
print("Student2: ", student2)

test_student2 = student2.friends[0].friends[0].friends[0]

student3 = Student(
    **{
        "name": "Marcy",
        "age": 27,
        "position": Point(1, 2),
        "friends": [
            Student(
                **{
                    "name": "Jared",
                    "age": 27,
                    "position": Point(1, 2),
                    "friends": []
                }
            )
        ]
    }
)
print("Student3: ", student3)

print(student["friends"][0]["friends"])
others_student = Student(name="jared", age=23, position=Point(1, 2))
print(student)
print(others_student)


@dataclass
class Person(TypedDict):
    name: str
    age: int
    position: Point
    friends: List["Student"]


person = Person(name="jared", age=23, position=Point(1, 2), friends=[])

TString = str
x: TString = "hey"

TStudentArgsDictKeys = Union[str, int, Point, List[Student]]
TStudentArgsDict = Dict[str, TStudentArgsDictKeys]

TAddableEntity = TypeVar("TAddableEntity")


def make_list_of_addable_entity(
        a: TAddableEntity,
        b: TAddableEntity,
) -> List[TAddableEntity]:
    return [a, b]


make_list_of_addable_entity(a=1, b=2)[0]
