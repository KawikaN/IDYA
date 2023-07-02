try:
    import pyautogui
    from interception import  *
    from constants import *
    from pytesseract import *
    from PIL import Image
except:
    print("There was an error trying to import the required files, check required.txt for the required libraries")


#955,100,20,20s
def poin(x, y, x2, y2):
    im4 = pyautogui.screenshot(region=(x,y,x2,y2)) #x, y(from top), width, height(down)
    im4.save(r'C:\Users\mnawe_000\Desktop\Idya\pics\Point2.png') #idk how to make it so that you can choose the file name
    print("PHOTO")
    #gets and stores image as Point2

#imge = Image.open(r'C:\Users\mnawe_000\Desktop\Idya\pics' + Fname)

def poin2(Fname, x, y, x2, y2):
    im4 = pyautogui.screenshot(region=(x,y,x2,y2)) #x, y(from top), width, height(down)
    im4.save(r'C:\Users\mnawe_000\Desktop\Idya\pics' + "\\" + Fname)