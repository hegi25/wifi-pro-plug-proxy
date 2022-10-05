import threading

from time import sleep

import http.server
from prometheus import *
from data import *
from mqtt import *
from inverter import *

threading.Thread(target=start_modbus).start()
threading.Thread(target=start_prometheus).start()
threading.Thread(target=start_mqtt).start()

