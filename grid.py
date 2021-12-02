from PIL import Image

from resizeImages import im1,im2,im3,im4,im5,im6,im7,im8,im9,im10,im11,im12,im13,im14,im15,im16
#from guessing import Alex, Aneesh, Annabel, Dashiell, Ellie, Evie, Grant, Hudson, Jack, Jonas, Kate, Kayla, Mina, Sam, Will, Yumn
import guessing
from PIL import Image, ImageDraw

def makeGrid():
    startGrid = Image.new('RGB', (725,725)) #creates a new empty image, RGB mode, and size 400 by 400.

    #Iterate through a 4 by 4 grid with 100 spacing, to place my image
    if guessing.Alex == True :
        startGrid.paste(im1, (25,25))
    if guessing.Aneesh == True:
        startGrid.paste(im2, (200,25))
    if guessing.Annabel == True :
        startGrid.paste(im3, (375,25))
    if guessing.Dashiell == True :
        startGrid.paste(im4, (550,25))
    if guessing.Ellie == True :
        startGrid.paste(im5, (25,200))
    if guessing.Evie == True :
        startGrid.paste(im6, (200,200))
    if guessing.Grant == True :
        startGrid.paste(im7, (375,200))
    if guessing.Hudson == True :
        startGrid.paste(im8, (550,200))
    if guessing.Jack == True :
        startGrid.paste(im9, (25,375))
    if guessing.Jonas == True :
        startGrid.paste(im10, (200,375))
    if guessing.Kate == True :
        startGrid.paste(im11, (375,375))
    if guessing.Kayla == True :
        startGrid.paste(im12, (550,375))
    if guessing.Mina == True :
        startGrid.paste(im13, (25,550))
    if guessing.Sam == True :
        startGrid.paste(im14, (200,550))
    if guessing.Will == True :
        startGrid.paste(im15, (375,550))
    if guessing.Yumn == True :
        startGrid.paste(im16, (550,550))
    startGrid.save("finalgrid.png")
    return startGrid

def numTrue():
    num = 0
    if guessing.Alex == True :
        num=num+1
    if guessing.Aneesh == True:
        num=num+1
    if guessing.Annabel == True :
        num = num + 1
    if guessing.Dashiell == True :
        num=num+1
    if guessing.Ellie == True :
        num=num+1
    if guessing.Evie == True :
        num=num+1
    if guessing.Grant == True :
        num = num + 1
    if guessing.Hudson == True :
        num=num+1
    if guessing.Jack == True :
        num=num+1
    if guessing.Jonas == True :
        num=num+1
    if guessing.Kate == True :
        num=num+1
    if guessing.Kayla == True :
        num=num+1
    if guessing.Mina == True :
        num=num+1
    if guessing.Sam == True :
        num=num+1
    if guessing.Will == True :
        num=num+1
    if guessing.Yumn == True :
        num = num + 1
    return num






