# AutoAuth
Auto login on **students.bmstu.ru** with reCAPTCHA bypass and grabbing all files from **students.bmstu.ru/teacher**

Actually, the URL can be changed, but it was created for the site above.

## Installation 

```ShellSession
$ git clone https://github.com/OzoNeTT/EUlogger
$ cd EUlogger
```

Create `./config/local.py` file and write the following into it

```Python
RUCAPTCHA_KEY = "API key from rucaptha.ru"
SITE_KEY = "site_key"
PAGE_URL = "URL"
DEBUG = False # Will not show browser, replace with True if you want to see the process
```

## Editing for personal use

Open `logger.py` and delete those lines:

```Python
...
from purple_entry.log import add_log
...
add_log(f'We have authorized {self.login}', 'INFO')
...
```
 

## Run

In EUlogger folder:

```ShellSession
$ ./deploy.sh ${LOGIN} ${PASSWORD}
```

## Developers

OzoNeTT: [VK](https://vk.com/ozonet_t), [GitHub](https://github.com/OzoNeTT)

Toliak Purple: [VK](https://vk.com/toliakpurple), [GitHub](https://github.com/Toliak)

