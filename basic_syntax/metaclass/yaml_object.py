import yaml


class Person(yaml.YAMLObject):
    yaml_tag = u'!Person'

    def __init__(self, name, gender, age, address):
        self.name = name
        self.gender = gender
        self.age = age
        self.address = address

    def __repr__(self):
        return "%s(name=%r, gender=%r, age=%r, address=%r)" % (
            self.__class__.__name__, self.name, self.gender, self.age,
            self.address
        )


yaml.load("""
--- !Person
name: Real
gender: male
age: 23
address: Home
""", Loader=yaml.FullLoader)

Person(name='Real', gender='male', age=23, address='Home')

print(yaml.dump(Person(name='Real', gender='male', age=23, address='Home')))
# !Person
# address: Home
# age: 23
# gender: male
# name: Real
