# Keylogger Project

This project serves as an example project for an ethical hacking course. It is designed to raise awareness and understanding of security vulnerabilities. **This project should not be used for any malicious purposes**.

## About the Project

The project includes a keylogger software that captures keystrokes on the user's computer. It is intended to demonstrate keystroke logging and highlight information security vulnerabilities.

## Usage

1. Download or clone the project source code.

2. Create a `settings.py` file in the root directory of the project.

3. Fill in the following fields in the `settings.py` file:

```python
sender_email = ''          # Email address of the sender
sender_password = ''       # Password of the sender's email account
receiver_email = ''        # Email address of the recipient
```
## Configuration

Make sure to provide the appropriate values for each field in the `settings.py` file:

- `sender_email`: Enter the email address of the sender. This should be the email address from which you want to send the captured keystrokes.

- `sender_password`: Enter the password of the sender's email account. This is the password for the email account used to send the captured keystrokes.

- The project trial was made between 2 gmail accounts. When you type your own password in your Gmail account, it does not accept it. To send mail on Python, gmail must provide you with a different password. You can solve the problem in this section with a few actions with the security settings of gmail.
- Error: smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted)
- Reference video link for error:
[[Watch the video]](https://www.youtube.com/watch?v=gOr-RQcfjMQ&ab_channel=Let%27sCodeMore)

- `receiver_email`: Enter the email address of the recipient. This is the email address where you want to receive the captured keystrokes.

**Note:** It is important to keep the `settings.py` file confidential and not share it publicly, as it contains sensitive information such as email credentials.

4. Install the necessary dependencies.

5. Run the `main.py` file to start the keylogger.

6. Use the provided methods to view or analyze the recorded keystrokes.

## Disclaimer

This project is for educational purposes only and should be used in compliance with legal permissions and ethical guidelines. Unauthorized collection of information or violation of someone's privacy is illegal. Before using the project, ensure that you comply with local laws and regulations.

