from PIL import Image
from resizeImages import im1,im2,im3,im4,im5,im6,im7,im8,im9,im10,im11,im12,im13,im14,im15,im16
from guessing import Alex, Aneesh, Annabel, Dashiell, Ellie, Evie, Grant, Hudson, Jack, Jonas, Kate, Kayla, Mina, Sam, Will, Yumn
from PIL import Image, ImageDraw

def makeGrid():
    startGrid = Image.new('RGB', (725,725)) #creates a new empty image, RGB mode, and size 400 by 400.

    #Iterate through a 4 by 4 grid with 100 spacing, to place my image
    if Alex == True :
        startGrid.paste(im1, (25,25))
    if Aneesh == True:
        startGrid.paste(im2, (200,25))
    if Annabel == True :
        startGrid.paste(im3, (375,25))
    if Dashiell == True :
        startGrid.paste(im4, (550,25))
    if Ellie == True :
        startGrid.paste(im5, (25,200))
    if Evie == True :
        startGrid.paste(im6, (200,200))
    if Grant == True :
        startGrid.paste(im7, (375,200))
    if Hudson == True :
        startGrid.paste(im8, (550,200))
    if Jack == True :
        startGrid.paste(im9, (25,375))
    if Jonas == True :
        startGrid.paste(im10, (200,375))
    if Kate == True :
        startGrid.paste(im11, (375,375))
    if Kayla == True :
        startGrid.paste(im12, (550,375))
    if Mina == True :
        startGrid.paste(im13, (25,550))
    if Sam == True :
        startGrid.paste(im14, (200,550))
    if Will == True :
        startGrid.paste(im15, (375,550))
    if Yumn == True :
        startGrid.paste(im16, (550,550))
    startGrid.save("finalgrid.png")
    return startGrid






