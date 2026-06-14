
from pathlib import Path
import configparser

class ConfigHelper:

    def __init__(self):
        self.config = configparser.ConfigParser()
        self._setup_config()

    def _setup_config(self):
        base_dir = Path(__file__).resolve().parent
        config_dir = base_dir / "config"
        
        dev_ini = config_dir / "dev.ini"
        if dev_ini.exists():
            self.config.read(dev_ini)
            print("Config file set up successfully")
        else:
            print("Could not find the dev ini file")


    def get(self, key: str):
        if self.config.has_option("settings", key):
            value = self.config.get("settings", key)
            return value

config = ConfigHelper()