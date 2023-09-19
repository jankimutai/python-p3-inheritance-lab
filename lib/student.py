#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self,last_name,first_name):
        super().__init__(last_name,first_name)
        self.knowledge = []
    def learn(self,my_knowledge):
        return self.knowledge.append(my_knowledge)