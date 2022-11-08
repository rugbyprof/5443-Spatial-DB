""" Background message passing app. Routes messages between players using a 
    keyword type schema. 
"""
import pika
import os,sys
import json
import time
import requests

class Comms(object):
    """ A helper class for client to client messaging. I don't know anything about
        pub/sub so this is rudimentary. In fact, it probably doesn't need to be a 
        class! However, I organized it into one simply for encapsulation, keeping 
        data and methods together and the added bonus of a constructor etc.
    """
    def __init__(self, **kwargs):
        """ Remember keyword arguments are params like: key=arg so order doesn't matter.
            The following example shows you how to init an instance of this class. 
        Example:
            {
                "exchange": "battleship",
                "port": "5672",
                "host": "battleshipgame.fun",
                "user": "yourteamname",
                "password": "yourpassword",
            }
        """
        self.exchange = kwargs.get("exchange", None)
        self.port = kwargs.get("port", 5432)
        self.host = kwargs.get("host", None)
        self.user = kwargs.get("user", None)
        self.password = kwargs.get("password", None)
        self.binding_keys = kwargs.get("binding_keys", [])
        
        self.establishConnection()

    def establishConnection(self,**kwargs):
        """ This method basically authenticates with the message server using:
        
                    host, port, user, and password
                    
            After authentication it chooses which "exchange" to listen to. This
            is just like a "channel" in slack. The exchange "type" = "topic" is 
            what allows us to use key_bindings to choose which messages to recieve
            based on keywords.
        """
        self.exchange = kwargs.get("exchange", self.exchange)
        self.port = kwargs.get("port", self.port)
        self.host = kwargs.get("host", self.host)
        self.user = kwargs.get("user", self.user)
        self.password = kwargs.get("password", self.password)
        
        if None in [self.exchange,self.port,self.host,self.user,self.password]:
            print("Error: connection parameter missing in class Comms mehod establishConnection!")
            sys.exit()
        
        credentials = pika.PlainCredentials(self.user, self.password)
        parameters = pika.ConnectionParameters(
            self.host, int(self.port), self.exchange, credentials
        )
        
        self.connection = pika.BlockingConnection(parameters)
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange=self.exchange, exchange_type="topic")



class CommsListener(Comms):
    def __init__(self, **kwargs):
        """ Extends Comms
        """
        self.binding_keys = kwargs.get("binding_keys", [])
        super().__init__(**kwargs)
        
        
    def bindKeysToQueue(self,binding_keys=None):
        """ https://www.rabbitmq.com/tutorials/tutorial-five-python.html

            A binding key is a way of "subscribing" to a specific messages. Without
            getting to the difference between "routing" and "topics" I will say topics
            should work better for battleship. Valid topics are things like:
               
               python.javascript.cpp
               
            This topic would receive any messages from queues containing the routing
            keys: `python` or `javascript` or `cpp`. You can register as many keys as you like.
            But you can also use wild cards:
            
                * (star) can substitute for exactly one word.
                # (hash) can substitute for zero or more words.
                
            So if you want to get all messages with your team involved:
                teamname.#
            Or if you want all messages that fire at you:
                teamname.fire.#
            
            Follow the link above to get a better idea, but at minimum you should
            add binding keys for anything with your teamname (or maybe id) in it.
                
        """
        result = self.channel.queue_declare("", exclusive=True)
        self.queue_name = result.method.queue
        
        if binding_keys == None and len(self.binding_keys) == 0:
            self.binding_keys = ["#"]
        elif binding_keys:
            self.binding_keys = binding_keys
            
        for binding_key in self.binding_keys:
            print(binding_key)
            self.channel.queue_bind(
                exchange=self.exchange, queue=self.queue_name, routing_key=binding_key
            )
            
    def startConsuming(self):
        self.channel.basic_consume(queue=self.queue_name, on_message_callback=self.callback, auto_ack=True)
        self.channel.start_consuming()
        
    def callback(self,ch, method, properties, body):
        print(f"{method.routing_key} : {body}")
        # logDict = {"routing_key": method.routing_key, "data": json.loads(body)}
        # with open("log.json", "a") as f:
        #     json.dump(logDict, f, indent=4)

class CommsSend(Comms):
    def __init__(self, **kwargs):
        """ Extends Comms and adds a "send" method which sends data to a 
            specified channel (exchange). 
        """
        super().__init__(**kwargs)
        
    def sendCommand(self,routing_key,command):
        self.channel.basic_publish(
            self.exchange, routing_key=routing_key, body=command)
    
    def closeConnection(self):
        self.connection.close()

def usage():
    print("Error: You need to choose `send` or `listen` and optionally `teamName`!")
    print("Usage: python CommsClass <send,listen> [teamName]")
    sys.exit()
    
def register(team,deleteFile=None):
    if deleteFile:
        if os.path.isfile("config.json"):
            os.remove("config.json")
    if not os.path.isfile("config.json"):
        key = '61ec12b68d0ded5f6a84b7d1f6d4d8e70695c2ba5dd7176fc3e4c3d53db9ecf2'
        r = requests.get(f"https://battleshipgame.fun:1234/register?team_name={team}&hash_key={key}")
        res = r.json()
        if res["success"]:
            with open("config.json","w") as f:
                json.dump(r.json(),f,indent=4)
                return r.json()
    
    with open("config.json") as f:
        data = json.load(f)
        
    return data
        

if __name__=='__main__':

    
    if len(sys.argv) < 2:
        usage()
    elif len(sys.argv) == 2:
        method = sys.argv[1]
    elif len(sys.argv) > 2:
        method = sys.argv[1]
        team = sys.argv[2]


    print(team)
    creds = register(team,"deletefile")
    
    print(creds)
    sys.exit()
        
    # creds = {'exchange':'battleship',
    #         'port':5672,
    #         'host':'battleshipgame.fun',
    #         'user':'admiral',
    #         'password':'rockpaperscissors'
    # }
        
    
    if method == 'send':
        commsSend = CommsSend(**creds)
        cmd = f"{team}.fire",json.dumps({"lat":34,"lon":-98,"bearing":231,"bags":8})
        print(cmd)
        commsSend.sendCommand(cmd[0],cmd[1])
        time.sleep(2)
        cmd = "broadcast.*","Hey everybody!!"
        print(cmd)
        commsSend.sendCommand(cmd[0],cmd[1])
        time.sleep(2)
        cmd = f"{team}.turn",f"{team} is turning!!"
        print(cmd)
        commsSend.sendCommand(cmd[0],cmd[1])
        commsSend.closeConnection()
    else:
        print("Comms Listener starting. To exit press CTRL+C ...")
        commsListener = CommsListener(**creds)
        commsListener.bindKeysToQueue([f'#.{team}.#','#.broadcast.#'])
        commsListener.startConsuming()






