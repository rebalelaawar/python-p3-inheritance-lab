#!/usr/bin/env python

from user import User

class Student(User):
    knowledge = []

    
    def learn(self,stri,knowledge=knowledge):
        self.knowledge = knowledge
        self.stri = stri
        self.knowledge.append(self.stri)
        