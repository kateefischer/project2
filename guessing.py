import pygame

#if true it means they have not yet been eliminated
Alex = True
Aneesh = True
Annabel = True
Dashiell = True
Ellie = True
Evie = True
Grant = True
Hudson = True
Jack = True
Jonas = True
Kate = True
Kayla = True
Mina = True
Sam = True
Will = True
Yumn = True

fullBoard = ["Alex", "Aneesh", "Annabel", "Dashiell", "Ellie", "Evie", "Grant", "Hudson", "Jack", "Jonas", "Kate", "Kayla", "Mina", "Sam", "Will", "Yumn"]
girls = ["Evie","Ellie","Annabel","Kate","Kayla","Mina"]
boys = ["Alex", "Aneesh", "Dashiell", "Grant", "Hudson", "Jack", "Jonas", "Sam", "Will", "Yumn"]
red = ["Hudson", "Dashiell", "Annabel", "Jonas"]
blue = ["Grant", "Aneesh", "Will"]
black = ["Alex", "Ellie", "Kate"]
gray = ["Jack"]
tan = ["Sam"]
white = ["Evie"]
purple = ["Mina"]
mint = ["Kayla", "Yumn"]
noTeeth = ["Sam", "Will"]
teeth = ["Alex", "Aneesh", "Annabel", "Dashiell", "Ellie", "Evie", "Grant", "Hudson", "Jack", "Jonas", "Kate", "Kayla", "Mina", "Yumn"]
brownHair = ["Jack", "Hudson", "Dashiell", "Alex", "Grant", "Evie", "Mina", "Ellie", "Will", "Jonas"]
blackHair = ["Annabel", "Aneesh", "Yumn"]
blondeHair = ["Kate", "Kayla", "Sam"]
curlyHair = ["Evie", "Mina", "Yumn"]




def guessChecker(list):
    if "Alex" in list:
        global Alex
        Alex = False
    if "Aneesh" in list:
        global Aneesh
        Aneesh = False
    if "Annabel" in list:
        print("In the list")
        global Annabel
        Annabel = False
    if "Dashiell" in list:
        global Dashiell
        Dashiell = False
    if "Ellie" in list:
        global Ellie
        Ellie = False
    if "Evie" in list:
        global Evie
        Evie = False
    if "Grant" in list:
        global Grant
        Grant = False
    if "Hudson" in list:
        global Hudson
        Hudson = False
    if "Jack" in list:
        global Jack
        Jack = False
    if "Jonas" in list:
        global Jonas
        Jonas = False
    if "Kate" in list:
        global Kate
        Kate = False
    if "Kayla" in list:
        global Kayla
        Kayla = False
    if "Mina" in list:
        global Mina
        Mina = False
    if "Sam" in list:
        global Sam
        Sam = False
    if "Will" in list:
        global Will
        Will = False
    if "Yumn" in list:
        global Yumn
        Yumn = False


