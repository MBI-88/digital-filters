#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 09:46:10 2018

@author: root
"""

from funcion import happyBirthday;

age = int(input("Age of the dog: "))

if age < 0:
	print("This can hardly be true!")
elif age == 1:
	print("about 14 human years")
elif age == 2:
	print("about 22 human years")
elif age > 2:
	human = 22 + (age -2)*5
	print("Human years: ", human)

happyBirthday("Bobby")