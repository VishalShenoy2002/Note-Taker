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

```bash
  pip install python-telegram-bot pillow PyPDF2 opencv-python
```
This will Install the required dependencies



## Deployment

To deploy this project run the following command

```bash
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



## FAQ

#### What do I need to run this software?

The mandatory requirements to run this software effectively is as follows
- **System Requirements**
    - Python 3.7 or above
    - Webcam or Camera
- Telegram Account

#### How do I create and deploy my own Telegram Bot?

 Refer this [link](https://sendpulse.com/knowledge-base/chatbot/telegram/create-telegram-chatbot) to create your own bot. 
 Then, create a file named ***botcred.txt*** and save you bot credentials in it. it should be present in the same directory as the ***note-taker.py*** file.
