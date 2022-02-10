## SafeQ - fast and easy-to-use password manager

<img src="https://i.ibb.co/tJYwK03/obraz-2022-02-10-172912.png" width="350"> <img src="https://i.ibb.co/kJC2Lf8/obraz-2022-02-04-222146.png" width="419">

## Description:
Credentials are encrypted using fernet encryption where first pbkdf2 hash of the password is used as the key and second hash is stored in db along with salt. This way even upon event of leaking your databases nobody will be able to use rainbow tables and brute-force the passwords.

SafeQ connects to your local database - feel free to play with credentials, just insert them in the program and make sure you have safeq database created.

## Requirements:
- MySql database named safeq
- packages installed from pyproject.toml

## Launching
(Windows) First add project folder to python path by:  
```set PYTHONPATH=C:\Users\User\path\to\safeq```  
Then:  
```python3 ./src/safeq.py```