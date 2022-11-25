import cv2
import datetime
import os
import telegram.bot

from PIL import Image
from PyPDF2 import PdfFileMerger


with open("botcred.txt","r") as f:
    API_TOKEN=f.read()
    f.close()


chat_id=input("Enter Chat ID: ")


images_to_covert=[]
stopped=False
# Passing 0 as an argument. 0 stands for primary camera

capture=cv2.VideoCapture(0)

while not stopped:

    _,frame=capture.read()
    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) & 0xFF==ord('c'):


        timestamp=datetime.datetime.today().now().strftime("%d%m%y %H%M%S")
        filename=f"{timestamp}.png"

        images_to_covert.append(filename)
        
        cv2.imwrite(filename, frame)

    
    if cv2.waitKey(1) & 0xFF==ord('q'):
        stopped=True

capture.release()
cv2.destroyAllWindows()

# Converting Images to PDF's and then Removing the Images
pdfs=[]
for image in images_to_covert:
    pdfname=image.split(".")[0]
    pdffilename=f"{pdfname}.pdf"
    imagedata=Image.open(image)
    pdfs.append(pdffilename)
    imagedata.save(pdffilename)
    imagedata.close()

# 
timestamp=datetime.datetime.today().strftime("%d%m%Y %H%M%S")
filename=f"{timestamp} - Notes.pdf"


for file in os.listdir(os.getcwd()):
    if file.endswith(".png"):
        os.remove(file)
        

merger=PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write(filename)
merger.close()
    
for file in os.listdir(os.getcwd()):
    if file in pdfs:
        os.remove(file)

bot=telegram.Bot(API_TOKEN)
# bot.send_message(chat_id, "Hello")

with open(filename,"rb") as f:
    bot.send_document(chat_id, f)
