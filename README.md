# Note-Taker

Note Taker is a software which will help students concentrate in class. It does this by reducing the burden of taking notes during class so that the students can listen to the class with full concentation.

## Installation

To install Note-Taker with git please use the following command:

```
  git clone https://github.com/VishalShenoy2002/Note-Taker.git
```
If you don't have git installed on your system, you can download the zip folder of this repository.

    
## Run Locally

To run the project locally on the system
- Locate the project folder and move into the project folder by using the following command:
```
  cd Note-Taker/
```


- Install dependencies

```
  pip install python-telegram-bot pillow PyPDF2 opencv-python
```
This will Install the required dependencies


To deploy this project run the following command

```
  python note-taker.py
```


## Tech Stack

This software uses Python 3.7 and uses the following modules
* Python Built-in Core Modules
    * datetime (Date and Time)
    * os (Operating System)

* Installed Packages (From PyPi)
    * cv2 (Computer Vision)
    * telegram
    * PIL (Python Image Library)
    * PyPDF2


## Usage

* When you first run the program, it asks you for a ***Chat ID***. 

* Once you enter the Chat ID then a screen with the Webcam broadcast will open. The user must press the ***'c' key*** to capture images of the board 'c' stands for Capture. 

* Once the Lecture is done the user must press the ***'q' key*** to quit the Webcam broadcast screen.

* Once the user presses the 'q' key the captured images will get converted into a PDF file and will be sent by the bot to the specified Chat ID.


## FAQ

#### What do I need to run this software?

The mandatory requirements to run this software effectively is as follows
- **System Requirements**
    - Python 3.7 or above
    - Webcam or Camera
- Telegram Account

#### As a teacher how do I set up this software?

 As a teacher, you need to first create a Telegram Bot. You can either create a group with all the students and add the bot to that group by giving the Chat ID of the group or you can get the individual Chat ID's of every student and send it individually.
 
 Create a file named ***botcred.txt*** and save you bot credentials in it. it should be present in the same directory as the ***note-taker.py*** file.

 Refer this [link](https://sendpulse.com/knowledge-base/chatbot/telegram/create-telegram-chatbot) to create your own bot. 

 Refer this [link](https://www.alphr.com/find-chat-id-telegram/) to get the Chat ID

