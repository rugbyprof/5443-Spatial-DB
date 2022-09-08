from random import shuffle

from time import sleep

from os import system

from rich import print

import time
from rich.progress import track



names=["Dowling, Byron",
"Warren, Allyson",
"kuruguntla, Madhuri",
"Kavuri, Prithvi Sai",
"Wilson, Dakota",
"Ejjina, Amulya",
"Konan, Loic",
"Sneath, Caleb",
"Thumar, Pramey",
"Hagmaier, Parker",
"Challa, Tejaswini",
"Jamakayala, Susheel",
"Md, Abubakkar",
"Yerra, Sai Pramod",
"Boyeena, Soundarya",
"Yanala, Srikanth Reddy",
"Mallareddy, Sahith Reddy",
"Sunkari, Naga Prashanth",
"Guneydas, Mihriban",
"Basani, Varshith",
"Dheke, Sabin",
"Brown, Deangelo"]

for i in track(range(50), description="Picking..."):
    shuffle(names)
    system('clear')
    print([names[0]])
    sleep(.2)





