# Note-Taker
Note Taker Application is a software which will help the students concentrate in class. It does this by reducing the burden of taking notes during class. The students can listen to the class with full concentation.

## Requirements
1. Note Taker is built using **Python 3.7**. So the users must have atleast **Python 3.6 or above** installed on his or her system.
2. The user must have a Telegram Account as the software will create a PDF and send it through telegram
3. A Camera or a Webcam that points towards the board. So that it can capture pictures of the board.

## Technical Details
As mentioned before this software uses Python 3.7 and uses the following modules:

* Python Built-in Core Modules
    * cv2 (Computer Vision)
    * datetime (Date and Time)
    * os (Operating System)

* Installed Packages (From PyPi)
    * telegram
    * PIL (Python Image Library)
    * PyPDF2

**Note:** Create a file named botcred.txt and save you bot credentials in it. it should be present in the same directory as the *note-taker.py* file. Refer this [link](https://sendpulse.com/knowledge-base/chatbot/telegram/create-telegram-chatbot) to create your own bot.

**Note:** For Installing the following Packages from PyPi run the following commands
```
pip install python-telegram-bot pillow PyPDF2
```

## How Does it Work?
Read the following Information to understand how the software works:
* The user must first run the program using the following command
```
python note-taker.py
```
* Once the user runs the program, it will ask the user to enter their telegram chat id which the user can find out by refering to this [link](https://www.alphr.com/find-chat-id-telegram/)

* After entering the chat id, there will be a broadcast of the webcam. If the user wants to capture the image he or she should **press the 'c' key** as 'c' stands for Capture. If the user wants to quit he or she should **press the 'q' key** as 'q' stands for Quit.

* Once the user quits the Camera Broadcast the images that the user has captured will get convertec into a PDF and will be sent on telegram to the Chat ID that the user mentioned