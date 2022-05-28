
# allow writt union types as X | Y 类型检查改进

from ctypes import Union
from typing import TypeAlias


# def old_func(param: Union[int, float]) -> Union[int, float]:
#     return param ** 2


def new_func(param: int | float) -> int | float:
    return param ** 2


# Explicit Type Aliases 类型别名的更改

# old version

old_name = str


def old_func(param: old_name) -> old_name:
    return param + param


# new version
new_name: TypeAlias = str


def new_func(param: new_name) -> new_name:
    return param + param


# dictionary is added a new property named mapping that used to return data of dict
my_dict = {
    "name": "Alice",
    "age": 23
}

keys = my_dict.keys()
values = my_dict.values()
items = my_dict.items()

print(keys.mapping)
print(values.mapping)
print(items.mapping)

# print
# {'name': 'Alice', 'age': 23}
# {'name': 'Alice', 'age': 23}
# {'name': 'Alice', 'age': 23}


# 函数 zip() 增加 strict 参数

keys = ["one", "two", "three"]

values = [1, 2, 3, 4]

# print(dict(zip(keys, values, strict=True)))

# Traceback (most recent call last):
#   File "C:\Users\Camille\Documents\Projects\practical-python\python-310-new-features.py", line 61, in <module>
#     print(dict(zip(keys, values, strict=True)))
# ValueError: zip() argument 2 is longer than argument 1
# (py3.10)


# 模板匹配

person1 = ("John", 36, "male")
person2 = ("Joe", 24, "famale")
person3 = ("Jane", 30, "actor")


def func(person):
    match person:
        case (name, _, "male"):
            print(f"{name} is man")
        case (name, _, "famale"):
            print(f"{name} is woman")
        case (name, age, gender):
            print(f"{name} is {age} old")


func(person1)
func(person2)
func(person3)

# John is man
# Joe is woman
# Jane is 30 old
