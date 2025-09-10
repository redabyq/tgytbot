# Telegram Bot for downloading video from youtube.com
[*Based on pytubefix*](https://pypi.org/project/pytubefix/)

## Installing 
### 1. Clone the repository
```bash
git clone https://github.com/redabyq/tgytbot
cd tgytbot
```
### 2.Create the virtual env
```bash
python3 -m venv ytenv
```
#### Windows
```cmd
ytenv\Scripts\activate
```
#### Linux
```bash
source ytenv\bin\activate
```
### 3. Install the requirements
```bash
pip install -r requirements.txt 
```
## Configuring 
If you open *config.json* you will see:
```json
{
    "token":"",
    "accept_ids":[],
    "allow_for_all":true,
    "videolimit":3600
}
```
__Token__ - Token of your bot. You will get it from [BotFather](https://t.me/BotFather)

__Accept IDs__ - Which Telegram users have access to your bot. You can get their IDs if you enable "Show Peer IDs" in Settings->Advanced in the Official Telegram Desktop Client

__Allow for all__ - *true* or *false*. Gives access for all users (if *true* __Accept IDs__ will be ignored). 

__Videolimit__ - limit for Youtube video lenth (in seconds)

### Example of *config.json*
```json
{
    "token":"0123456789:abcdefghijklmnopqrstuvwxyz",
    "accept_ids":[0000000000,1111111111,2222222222],
    "allow_for_all":false,
    "videolimit":3600
}
```
## Running
```bash
python app.py
```

That's all, have a good day

![thankyou](https://avatars.mds.yandex.net/get-yapic/59871/P1BrP36tHy9fUQE15gdowXRr1E-1/orig)
