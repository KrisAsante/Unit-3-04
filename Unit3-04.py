# Created by: Chris Asante
# Created on: 07-Mar-2019
# Created for: ICS3U
# Unit 3-04
# This program calculates a leap year

from tkinter import *

year=int(input("choose a year?"))
if (year%4==0 and year%100!=0 or year%400==0):
    print("this year will be a leap")
else:
    print("this year will not be a leap year")