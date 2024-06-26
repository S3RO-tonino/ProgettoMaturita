import RPi.GPIO as gp
from datetime import datetime

gp.setmode(gp.BCM)

gp.setup(17, gp.IN)

def leggiDati():
    try:
        data = {}
        if gp.input(17): isIntrusion = True
        else: isIntrusion = False
        mex = datetime.now().strftime('%H:%M:%S')
    except Exception as e: mex=(f"errore: {e}")

    data = {"ID": 'MSensor', "name": 'MSensor', "intrusion": isIntrusion, "mex": f'{mex}'}
    return data
