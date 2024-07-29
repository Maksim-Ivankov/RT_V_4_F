from variable import *
from imports import *


class Save_config():
    def __init__(self,sections_name,list_key_value):
        super().__init__()
        
        config = configparser.ConfigParser()
        config.read(path_imports_config)

        if (sections_name) in config.sections():
            for key, value in list_key_value.items():
                config.set(sections_name, key,value)
            with open(path_imports_config, 'w') as configfile:
                config.write(configfile)
        else: 
            config[sections_name] = list_key_value
            with open(path_imports_config, 'w') as configfile:
                config.write(configfile)
    
    







