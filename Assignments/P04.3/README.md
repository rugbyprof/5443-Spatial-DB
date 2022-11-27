## Project 4.3 - Comms and Menu
#### Due: 12-01-2022 (Thursday @ 3:30 p.m.)

## Overviewgit 

This assignment has two major components: messaging and menu

You will need to get the communication pathways handled: sending and receiving messages from our RabbitMQ backend. You will also need to generate your menu system to communicate with the game. Preferably your menu, and message handler can share the same terminal. I will leave that up to you to figure out. Next lets look at the comms classes.


## Comms

The comms classes are available in this folder here:
- [comms.py](./commsCode/comms.py)
- [listener.py](./commsCode/listener.py)
- [sender.py](./commsCode/sender.py)

### Discussion
- I hope each file has enough comments to get you started, but if not just ask me. 
- The `comms.py` file is just a base class for both `listener` and `sender`
- The `listener` does just that, it sits and waits for messages that have its fleet name in it and prints those messages to the screen.
- The `sender` has a rudimentary menu system that is horrible. I threw it in there simply as something to run. 
- The format I use in the `sender` to actually send commands is not something I will use! Sending commands will all be handled by api routes.
- This another reason I gave you the json file, so you could at least use 

## Menu

- The menu you options to interact with the "game" are defined in this local file [menu.json](./menu.json).
- Each item in the menu will match up to an api route, with exactly the same definitions That's why I put the effort in providing examples and descriptions within that file.
- You will need to create your own menu driven system, that incorporates the menu items and function handlers. 
- For example:

```python
import requests
# every route needs your hash wether its in the docs or not
url = f'https://battleshipgame.fun/battleLocation/?hash=yourprivatehashkey&fleet_id=us_navy'

r = requests.get(url)
if r.status_code == requests.codes.ok:
    responseData = r.json() 
    print(responseData)
```
will print

```python
    {
        "bbox": {
                "UpperLeft": "{'lon':dd.ffffffff,'lat':dd.ffffffff}",
                "LowerRight": "{'lon':dd.ffffffff,'lat':dd.ffffffff}"
            },
        "CardinalLocation": "SSE"
    }
        
```

For more complicated commands, here is an example `moveGuns` route:

```python
import requests
import json

url = "https://battleshipgame.fun:1234/moveGuns/"

payload = json.dumps({
    "fleet_id": 11,
    "ship_id": [
        0,
        1,
        2
    ],
    "gun_id": [
        [
            0,
            1,
            2,
            3
        ],
        [
            3,
            4,
            5
        ],
        [
            1,
            2,
            3
        ]
    ],
    "gun_position": [
        [
            [
                [
                    90,
                    30
                ],
                [
                    90,
                    30
                ],
                [
                    90,
                    30
                ],
                [
                    90,
                    30
                ]
            ]
        ],
        [
            [
                [
                    120,
                    40
                ],
                [
                    120,
                    40
                ],
                [
                    120,
                    40
                ]
            ]
        ],
        [
            [
                [
                    320,
                    40
                ],
                [
                    320,
                    40
                ],
                [
                    320,
                    40
                ]
            ]
        ]
    ]
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
```

- Here is a list of python library's that help generate menus:
    - https://github.com/wong2/pick
    - https://github.com/aegirhall/console-menu
    - https://github.com/IngoMeyer441/simple-term-menu
    - https://github.com/prompt-toolkit/python-prompt-toolkit
    - https://github.com/pallets/click/


### Deliverables

- Create a folder called `P04.3` in your assignments folder.
- Place your menu / comms code in this folder with a README that describes its usage and supporting libraries or additional files used. 


