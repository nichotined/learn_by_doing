from dataclasses import dataclass

@dataclass
class person(object):
    name: str
    age: int

person1 = person('Nicholas Frederick', 21)
print(person1.name)
print(person1.age)
