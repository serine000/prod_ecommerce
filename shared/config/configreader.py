import configparser
from pathlib import Path

_config = configparser.ConfigParser()
_config.read(Path(__file__).parent / "config.ini")

def get(section: str, key: str, fallback=None) -> str:
    return _config.get(section, key, fallback=fallback)

def get_int(section: str, key: str, fallback=None) -> str:
    return _config.getint(section, key, fallback=fallback)

def get_bool(section: str, key: str, fallback=None) -> str:
    return _config.getbool(section, key, fallback=fallback)