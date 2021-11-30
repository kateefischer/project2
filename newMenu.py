from PIL import Image
import guessing
from grid import startGrid
import game

fullGrid = Image.new('RGB', (1000,1000))
fullGrid.paste(startGrid, 0,0)