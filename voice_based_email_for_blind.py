# Project: Voice based Email for blind

import speech_recognition as sr
import smtplib
from bs4 import BeautifulSoup
import email
import imaplib
from gtts import gTTS
import pyglet
import os, time



# Fetch project name
tts = gTTS(text="Project: Voice based Email for blind.  This project is developed by Aman to help the blind access their mails and assist them.", lang='en')
ttsname = "name.mp3"
tts.save(ttsname)

music = pyglet.media.load(ttsname, streaming=False)
music.play()

time.sleep(music.duration)
os.remove(ttsname)

# Login from OS
login = os.getlogin
print("                                                            Voice based Email for blind \n Developed By :\n1. Aman Singh\n2. Ayush Karn\n3. Karan Sharma\n4. Vikash Kumar\n5. Madhur Gupta\n\n ")
print("\nYou are logging from:", login())

# Choices
print("\nWhat do you want to perform? \n\nSpeak out one of the promted options to proceed.")
tts = gTTS(text="What do you want to perform? Speak out one of the promted options to proceed.", lang='en')
ttsname = "speak.mp3"
tts.save(ttsname)

music = pyglet.media.load(ttsname, streaming=False)
music.play()

time.sleep(music.duration)
os.remove(ttsname)

print("\n1. Compose a mail.")
tts = gTTS(text="Option 1. Compose a mail.", lang='en')
ttsname = "hello.mp3"
tts.save(ttsname)

music = pyglet.media.load(ttsname, streaming=False)
music.play()

time.sleep(music.duration)
os.remove(ttsname)

print("2. Check your inbox.")
tts = gTTS(text="Option 2. Check your inbox.", lang='en')
ttsname = "second.mp3"
tts.save(ttsname)

music = pyglet.media.load(ttsname, streaming=False)
music.play()

time.sleep(music.duration)
os.remove(ttsname)

print("3. Search a mail.")
tts = gTTS(text="Option 3. Search a mail.", lang='en')
ttsname = "search.mp3"
tts.save(ttsname)

music = pyglet.media.load(ttsname, streaming=False)
music.play()

time.sleep(music.duration)
os.remove(ttsname)

print("4. Read the last mail.")
tts = gTTS(text="Option 4. Read the last mail.", lang='en')
ttsname = "read1.mp3"
tts.save(ttsname)

music = pyglet.media.load(ttsname, streaming=False)
music.play()

time.sleep(music.duration)
os.remove(ttsname)



print("5. Delete a mail")
tts = gTTS(text="Option 5. Delete a mail.", lang='en')
ttsname = "delete.mp3"
tts.save(ttsname)

music = pyglet.media.load(ttsname, streaming=False)
music.play()

time.sleep(music.duration)
os.remove(ttsname)

print("6. Get the last 3 mails.")
tts = gTTS(text="Option 6. Get the last 3 mails.", lang='en')
ttsname = "last.mp3"
tts.save(ttsname)

music = pyglet.media.load(ttsname, streaming=False)
music.play()

time.sleep(music.duration)
os.remove(ttsname)


# Voice recognition part
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Your choice:")
        audio = r.listen(source)
        print("Ok done!")

    try:
        text = r.recognize_google(audio)
        print("\nYou said:", text)
        return text.lower()
    except sr.UnknownValueError:
        print("\nGoogle Speech Recognition could not understand audio.")
    except sr.RequestError as e:
        print("\nCould not request results from Google Speech Recognition service; {0}".format(e))

# def get_audio():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Your choice:")
#         audio = r.listen(source)
#         print("Ok done!")

#     try:
#         text = r.recognize_google(audio)
#         print("You said:", text)

#         # Convert text to speech
#         tts = gTTS("You have selected option " + text)
#         tts.save("selected_option.mp3")

#         # Play the speech
#         music = pyglet.media.load(ttsname, streaming=False)
#         music.play()

#         return text.lower()
#     except sr.UnknownValueError:
#         print("Google Speech Recognition could not understand audio.")
#     except sr.RequestError as e:
#         print("Could not request results from Google Speech Recognition service; {0}".format(e))


# Choices details
text = get_audio()

if text == '1' or text == 'one':
    r = sr.Recognizer()
    with sr.Microphone() as source:
        tts = gTTS(text="Speak out the message you want to send.", lang='en')
        ttsname = "name1.mp3"
        tts.save(ttsname)

        music = pyglet.media.load(ttsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(ttsname)


        print("\nYour message:")
        audio = r.listen(source)
        print("\nOk done!")

    try:
        text1 = r.recognize_google(audio)
        print("\nYou said:", text1)
        msg = text1
    except sr.UnknownValueError:
        print("\nGoogle Speech Recognition could not understand audio.")
    except sr.RequestError as e:
        print("\nCould not request results from Google Speech Recognition service; {0}".format(e))

    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login('Your email id', 'password')
    mail.sendmail('Your email id', 'Target email id', msg)
    
    print("\nCongratulations! Your mail has been sent.")
    tts = gTTS(text="Congratulations! Your mail has been sent.", lang='en')
    ttsname = "send.mp3"
    tts.save(ttsname)
    music = pyglet.media.load(ttsname, streaming=False)
    music.play()
    time.sleep(music.duration)
    os.remove(ttsname)
    mail.close()

elif text == '2' or text == 'two':
    mail = imaplib.IMAP4_SSL('imap.gmail.com', 993)
    unm = 'Your email id'
    psw = 'password'
    mail.login(unm, psw)
    mail.select('INBOX')
    _, data = mail.search(None, 'ALL')
    mail_ids = data[0]
    id_list = mail_ids.split()
    latest_emails = id_list[-3:]
    for num in latest_emails:
        _, email_data = mail.fetch(num, '(RFC822)')
        raw_email = email_data[0][1].decode("utf-8")
        email_message = email.message_from_string(raw_email)
        print("\nFrom: " + email_message['From'])
        print("\nSubject: " + str(email_message['Subject']))
        tts = gTTS(text="From: " + email_message['From'] + " Subject: " + str(email_message['Subject']), lang='en')
        ttsname = "mail.mp3"
        tts.save(ttsname)
        music = pyglet.media.load(ttsname, streaming=False)
        music.play()
        time.sleep(music.duration)
        os.remove(ttsname)

    mail.logout()

# elif text == '2' or text == 'two':
#     mail = imaplib.IMAP4_SSL('imap.gmail.com', 993)
#     unm = 'Your email id'
#     psw = 'password'
#     mail.login(unm, psw)
#     mail.select('INBOX')
#     _, data = mail.search(None, 'ALL')
#     mail_ids = data[0]
#     id_list = mail_ids.split()
#     latest_emails = id_list[-3:]
#     for num in latest_emails:
#         _, email_data = mail.fetch(num, '(RFC822)')
#         raw_email = email_data[0][1].decode("utf-8")
#         email_message = email.message_from_string(raw_email)
#         print("From: " + email_message['From'])
#         print("Subject: " + str(email_message['Subject']))
#         tts_text = "From: " + email_message['From'] + ". Subject: " + str(email_message['Subject'])
        
#         # Read the body of the email
#         if email_message.is_multipart():
#             for part in email_message.walk():
#                 if part.get_content_type() == 'text/plain':
#                     body = part.get_payload(decode=True).decode('utf-8')
#                     tts_text += ". Body: " + body
#                     break
#         else:
#             body = email_message.get_payload(decode=True).decode('utf-8')
#             tts_text += ". Body: " + body

#         tts = gTTS(text=tts_text, lang='en')
#         tts.save("mail.mp3")
#         os.system("mpg123 mail.mp3")

#     mail.logout()


elif text == '3' or text == 'three':
    mail = imaplib.IMAP4_SSL('imap.gmail.com', 993)
    unm = 'Your email id'
    psw = 'password'
    mail.login(unm, psw)
    mail.select('INBOX')

    tts = gTTS(text="Please say the keyword to search for:", lang='en')
    ttsname = "search_keyword.mp3"
    tts.save(ttsname)
    music = pyglet.media.load(ttsname, streaming=False)
    music.play()
    time.sleep(music.duration)
    os.remove(ttsname)

    keyword = get_audio()
    _, data = mail.search(None, 'ALL')
    mail_ids = data[0]
    id_list = mail_ids.split()
    search_results = []
    for num in id_list:
        _, email_data = mail.fetch(num, '(RFC822)')
        raw_email = email_data[0][1].decode("utf-8")
        email_message = email.message_from_string(raw_email)
        if keyword.lower() in str(email_message).lower():
            search_results.append(email_message)

    if len(search_results) > 0:
        print("\nSearch Results:")
        tts = gTTS(text="Search Results:", lang='en')
        ttsname = "search_results.mp3"
        tts.save(ttsname)
        music = pyglet.media.load(ttsname, streaming=False)
        music.play()
        time.sleep(music.duration)
        os.remove(ttsname)

        for result in search_results:
            print("\nFrom: " + result['From'])
            print("\nFrom: " + result['From'])
            tts = gTTS(text="From: " + result['From'] + " Subject: " + str(result['Subject']), lang='en')
            ttsname = "result.mp3"
            tts.save(ttsname)
            music = pyglet.media.load(ttsname, streaming=False)
            music.play()
            time.sleep(music.duration)
            os.remove(ttsname)

    else:
        print("\nNo results found for the keyword: " + keyword)
        tts = gTTS(text="No results found for the keyword: " + keyword, lang='en')
        ttsname = "no_results.mp3"
        tts.save(ttsname)
        music = pyglet.media.load(ttsname, streaming=False)
        music.play()
        time.sleep(music.duration)
        os.remove(ttsname)

    mail.logout()

elif text == '6' or text == 'six':
    mail = imaplib.IMAP4_SSL('imap.gmail.com', 993)
    unm = 'Your email id'
    psw = 'password'
    mail.login(unm, psw)
    mail.select('INBOX')
    _, data = mail.search(None, 'ALL')
    mail_ids = data[0]
    id_list = mail_ids.split()
    latest_emails = id_list[-3:]
    for num in latest_emails:
        _, email_data = mail.fetch(num, '(RFC822)')
        raw_email = email_data[0][1].decode("utf-8")
        email_message = email.message_from_string(raw_email)
        print("From: " + email_message['From'])
        print("Subject: " + str(email_message['Subject']))
        tts = gTTS(text="From: " + email_message['From'] + " Subject: " + str(email_message['Subject']), lang='en')
        ttsname = "mail.mp3"
        tts.save(ttsname)
        music = pyglet.media.load(ttsname, streaming=False)
        music.play()
        time.sleep(music.duration)
        os.remove(ttsname)

    mail.logout()

elif text == '5' or text == 'five':
    mail = imaplib.IMAP4_SSL('imap.gmail.com', 993)
    unm = 'Your email id'
    psw = 'password'
    mail.login(unm, psw)
    mail.select('INBOX')
    _, data = mail.search(None, 'ALL')
    mail_ids = data[0]
    id_list = mail_ids.split()
    
    if len(id_list) > 0:
        print("\nEnter the number of the mail you want to delete:")
        tts = gTTS(text="Enter the number of the mail you want to delete.", lang='en')
        ttsname = "delete_prompt.mp3"
        tts.save(ttsname)
        music = pyglet.media.load(ttsname, streaming=False)
        music.play()
        time.sleep(music.duration)
        os.remove(ttsname)
        
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening for mail number...")
            audio = r.listen(source)
            print("Ok done!")
            
        try:
            mail_number = int(r.recognize_google(audio))
            if mail_number > 0 and mail_number <= len(id_list):
                mail.delete(id_list[mail_number - 1])
                print("Mail successfully deleted.")
                tts = gTTS(text="Mail successfully deleted.", lang='en')
                ttsname = "mail_deleted.mp3"
                tts.save(ttsname)
                music = pyglet.media.load(ttsname, streaming=False)
                music.play()
                time.sleep(music.duration)
                os.remove(ttsname)
            else:
                print("Invalid mail number. Please try again.")
                tts = gTTS(text="Invalid mail number. Please try again.", lang='en')
                ttsname = "invalid_mail_number.mp3"
                tts.save(ttsname)
                music = pyglet.media.load(ttsname, streaming=False)
                music.play()
                time.sleep(music.duration)
                os.remove(ttsname)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio.")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
    else:
        print("No mails found in your inbox.")
        tts = gTTS(text="No mails found in your inbox.", lang='en')
        ttsname = "no_mails.mp3"
        tts.save(ttsname)
        music = pyglet.media.load(ttsname, streaming=False)
        music.play()
        time.sleep(music.duration)
        os.remove(ttsname)

    mail.expunge()
    mail.close()
    mail.logout()

elif text == '4' or text == 'four':
    mail = imaplib.IMAP4_SSL('imap.gmail.com', 993)
    unm = 'Your email id'
    psw = 'qbjndjjqlceuwfsc'
    mail.login(unm, psw)
    mail.select('INBOX')
    _, data = mail.search(None, 'ALL')
    mail_ids = data[0]
    id_list = mail_ids.split()
    latest_email_id = id_list[-1]  # Get the last email ID
    _, email_data = mail.fetch(latest_email_id, '(RFC822)')
    raw_email = email_data[0][1].decode("utf-8")
    email_message = email.message_from_string(raw_email)
    print("\nFrom: " + email_message['From'])
    print("\nSubject: " + str(email_message['Subject']))
    tts_text = "\nFrom: " + email_message['From'] + ". Subject: " + str(email_message['Subject'])

    # Read the body of the email
    if email_message.is_multipart():
        for part in email_message.walk():
            if part.get_content_type() == 'text/plain':
                body = part.get_payload(decode=True).decode('utf-8')
                tts_text += ". Body: " + body
                break
    else:
        body = email_message.get_payload(decode=True).decode('utf-8')
        tts_text += ". Body: " + body

    tts = gTTS(text=tts_text, lang='en')
    ttsname = "lastmail.mp3"
    tts.save(ttsname)
    music = pyglet.media.load(ttsname, streaming=False)
    music.play()
    time.sleep(music.duration)
    os.remove(ttsname)
    mail.close()

    mail.logout()




else:
    print("\nInvalid choice. Please try again.")
    tts = gTTS(text="Invalid choice. Please try again.", lang='en')
    ttsname = "invalid_choice.mp3"
    tts.save(ttsname)
    music = pyglet.media.load(ttsname, streaming=False)
    music.play()
    time.sleep(music.duration)
    os.remove(ttsname)













# tts = gTTS(text="Speak out the message you want to send.", lang='en')
#         ttsname = "name1.mp3"
#         tts.save(ttsname)

#         music = pyglet.media.load(ttsname, streaming=False)
#         music.play()

#         time.sleep(music.duration)
#         os.remove(ttsname)

