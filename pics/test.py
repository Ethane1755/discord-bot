import os
import random 

path="D:/USER/Documents/GitHub/Code/Python/Discord/pics"
files=os.listdir(path)
d=random.choice(files)
os.startfile("D:/USER/Documents/GitHub/Code/Python/Discord/pics/"+d)