import socket
from cache import Cache
from parser_config import Parser_Config
from logs import Logs
from query import Query
import threading
import sys
import time


ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.connect(("127.0.0.1", 2001))
print(f"[SS] - SERVER CONNECTED")
        