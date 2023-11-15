#!/usr/bin/env python

from user import User

import random


class Teacher(User):

    knowledge = ["str is a data type in Python",
    "programming is hard, but it's worth it",
    "JavaScript async web request",
    "Python function call definition",
    "object-oriented teacher instance",
    "programming computers hacking learning terminal",
    "pipenv install pipenv shell",
    "pytest -x flag to fail fast",]

   

    def _init__(self, first_name, last_name, knowledge):
        super().__init__(first_name, last_name)
    

    def teach(self):
        return (self.knowledge[random.randint(0, len(self.knowledge)-1)])
        