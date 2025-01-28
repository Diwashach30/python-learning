# use of label and pack as a attributes in python in GUI

from tkinter import *

root = Tk()
root.geometry("600x600")
root.title("Deepseek GUI")

## Important label options

# 1. text - adds text
# 2. bg - add background
# 3. fg - foreground
# 4. font - add font
# 5. padx - padding x
# 6. pady - padding y
# 7. width - 
# 8. height
# 9. borderwidth - border width
# 10. relief - border style
# 11. anchor - anchor position
# 12. side - side position
# 13. image - add image
# 14. fill - fill style
 
title_label = Label( text='''DeepSeek-V3 uses significantly fewer resources compared to its peers; \n for example, whereas the world’s leading A.I. companies train their chatbots with supercomputers using as many as 16,000 \n integrated circuits ("computer chips"), if not more, DeepSeek claims to have needed only about 2,000  \n specialized computer chips, namely the H800 series from American multinational technology company Nvidia. It \n was trained in around 55 days at a cost of US$5.58 million,[37] \n  which is roughly 10 times less than what U.S. tech giant Meta spent building its latest A.I. technology.''', bg= "red" , fg= "white", padx= "10", pady = "10" , font= "comicsansms 12 bold",  relief= "groove" )  
title_label.pack(side=LEFT,   fill= "x")

root.mainloop()