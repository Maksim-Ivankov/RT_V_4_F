
from flet_translator import TranslateFletPage, GoogleTranslateLanguage
import requests
from email_validator import validate_email, EmailNotValidError
import json
import configparser
import os.path
import shutil
import time
import threading
import matplotlib.pyplot as plt
import squarify
from flet.matplotlib_chart import MatplotlibChart
from binance.um_futures import UMFutures
import pandas as pd
import io
from ast import literal_eval
import random
import statsmodels.api as sm
import flet.canvas as cv
import math
from datetime import datetime
import mplfinance as mpf
import talib as ta
from talib import abstract

import numpy as np

# from flet_multi_page import subPage

# работа с тг
from xmlrpc.client import DateTime
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import PeerChannel

# игнорим предупреждения
import warnings
warnings.filterwarnings("ignore")

