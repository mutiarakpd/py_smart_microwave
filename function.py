from os import system, name
from time import sleep

# Jika dipencet maka jadi true
microwave=False
grill=False
oven=False
steam=False
crispy=False
wattage=300
temperature=70
displayedwatt=False
displayedtemp=False
high=False
medium=False
low=False
refillWater=False

def displayWatt():
    global displayedwatt
    displayedwatt=True
    print(wattage)

def displayTemp():
    global displayedtemp
    displayedtemp=True
    print(temperature)

def modeHigh():
    global high,medium,low
    if high==True:
        high=False
    else:
        high=True
        medium=False
        low=False

def modeMedium():
    global high,medium,low
    if medium==True:
        medium=False
    else:
        high=False
        medium=True
        low=False

def modeLow():
    global high,medium,low
    if low==True:
        low=False
    else:
        high=False
        medium=False
        low=True

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def increase():
    global wattage, temperature
    if displayedwatt==True:
        clear()
        wattage+=100
        displayWatt()
    elif displayedtemp==True:
        clear()
        temperature+=10
        displayTemp()
    
def decrease():
    global wattage, temperature
    if displayedwatt==True:
        clear()
        wattage-=100
        displayWatt()
    elif displayedtemp==True:
        clear()
        temperature-=10
        displayTemp()

def micro():
    global microwave
    if microwave==False:
        microwave=True
    else:
        microwave==False


    