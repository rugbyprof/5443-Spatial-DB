import pika
import json
import requests
from random import shuffle
from rich import print


config = {
    'exchange':'battleship',
    'port':'5672',
    'host':'battleshipgame.fun',
    'user':'admiral',
    'password':'rockpaperscissors'
}

def sendCommand(routing_key,command):

    credentials = pika.PlainCredentials(config['user'], config['password'])
    parameters = pika.ConnectionParameters(config['host'],
                                        int(config['port']),
                                        config['exchange'],
                                        credentials)

    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    channel.exchange_declare(exchange=config['exchange'], exchange_type='topic')

    channel.basic_publish(
        config['exchange'], routing_key=routing_key, body=command)

    print(f" [x] Sent {routing_key}, {command}")

    connection.close()


def getMenu():
    r = requests.get("https://battleshipgame.fun:1234/game_menu/")
    return r.json()

def getMenuItems(menu):
    i = 1
    strmenu = ""
    for item in menu:
        strmenu += f"{i}. {item['item']}\n"
        i += 1
        
    return strmenu

def getMenuParams(menu,choice):
    return menu[choice]["params"]

    # routing_keys = ['one.fire','two.fire']
    # shuffle(routing_keys)

fleets = ['allies','axis','kriegsmarine']


while True:
    menu = getMenu()
    i = 0
    for fleet in fleets:
        print(f"{i}. {fleet}")
        i += 1
    target = int(input(":"))
    print(getMenuItems(menu))
    choice = input(":")
    if int(choice) == 1:
        print("register")
    else:
        print(getMenuParams(menu,int(choice)-1))
        params = input()
        print(params)
        
    cmd = menu[int(choice)-1]['key']
    print(cmd)
    sendCommand(f"{fleets[target]}.{cmd}",json.dumps({"lat":34,"lon":-98,"bearing":231,"bags":8}))
    
    
