# encoding: utf-8

from abc import ABCMeta, abstractmethod


class Entity(metaclass=ABCMeta):
    @abstractmethod
    def get_title(self):
        pass

    @abstractmethod
    def set_title(self, title):
        pass


class Document(Entity):
    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title


document = Document()
document.set_title('Harry Potter')
print(document.get_title())
# Harry Potter

entity = Entity()
entity.get_title()
# Traceback (most recent call last):
# File "C:\Users\AbstractClass.py", line 27, in <module>
#     entity = Entity()
# TypeError: Can't instantiate abstract class Entity with abstract methods get_title, set_title
