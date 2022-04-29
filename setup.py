from setuptools import setup, find_packages

setup(
    name = "python-bale-bot",
    version = "2.1.5.2",
    platforms = ["Windows"],
    fullname = "python-bale-bot-api",
    description = "The official repository of the programming of «Bale bot»",
    author = "Kian Ahmadian",
    license = "MIT License",
    project_urls = {
        "Source Code": "https://github.com/kianahmadian/python-bale-bot/blob/main/balebot",
        "Documentation": "https://python-bale-bot.readthedocs.io/en/latest/",
        "Bug Tracker": "https://github.com/kianahmadian/python-bale-bot/issues"
    },
    keywords = ["bale", "bot", "baleapi"],
    python_requires = '>=3.8',
    include_package_data = True,
    url = "https://github.com/kianahmadian/python-bale-bot/",
    packages = find_packages(),
    long_description = """<div align='center'>
<h1><b> Bale Bot </b></h1>

[![All Contributors](https://img.shields.io/github/contributors/kianahmadian/python-bale-bot)](#contributors-)
![Pull Requests](https://img.shields.io/github/issues-pr/kianahmadian/python-bale-bot?)
![Forks](https://img.shields.io/github/forks/kianahmadian/python-bale-bot)
![Stars](https://img.shields.io/github/stars/kianahmadian/python-bale-bot)
![License](https://img.shields.io/github/license/kianahmadian/python-bale-bot)
  
## 🗃 Table of contents
</div>

* [Info](https://github.com/kianahmadian/python-bale-bot/#%E2%84%B9-info)
* [Files](https://github.com/kianahmadian/python-bale-bot/#-files)
* [Installing](https://github.com/kianahmadian/python-bale-bot/#-installing)
* [Social Media](https://github.com/kianahmadian/python-bale-bot/#-social-media)
* [More Info](https://github.com/kianahmadian/python-bale-bot/#-more-info)


<div align='center'>

## `ℹ` Info 

سلام دوستان عزیز امیدوارم حالتون خوب باشه 

این پکیج جهت راحتی استفاده از وب سرویس های [بله](https://bale.ai/) می باشد

## `🗂` Files 

</div>

### `📜` License 
* [MIT License](https://github.com/kianahmadian/python-bale-bot//blob/main/LICENSE)

### `⚙` Setup Files 
* [setup (Python)](https://github.com/kianahmadian/python-bale-bot//blob/main/setup.py)
* [setup (cfd)](https://github.com/kianahmadian/python-bale-bot//blob/main/setup.cfd)


<div align='center'>

## `⬇` Installing 

### with Git:

```
pip install git+https://github.com/kianahmadian/python-bale-bot/ -U
```

### with PyPi:

```
pip install python-bale-bot -U
```

</div>

<div align='center'>

## `📡` More Info

</div>

* [وب سایت بله](https://bale.ai/)
* [سایت برنامه نویسان بله](https://devbale.ir/)
* [وب سرویس های بله](https://devbale.ir/api/)
* [بات ساخت بات در بله](https://ble.ir/@botfather)

<div align='center'>

## `📚` Social Media

<a href="https://discord.com/users/684748470799958033"> Discord </a>

</div>
""",
    long_description_content_type='text/markdown',
    install_requires = [
"aiohttp==2.3.7",
"async-timeout==2.0.0",
"asyncio==3.4.3",
"requests==2.26.0"]
)

print(r"""
____    __        ____   ____  ____  _____
|___|  /__\  |    |___   |___| |   |   |
|___| /    \ |___ |___   |___| |___|   |

""")