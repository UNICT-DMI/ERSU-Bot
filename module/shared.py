"""Constants and common functions"""
from typing import TypedDict
import logging
import yaml

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def read_md(namefile: str) -> str:
    """ Read a markdown file

    Args:
        namefile: name of the markdown file without extension

    Returns:
        content of the markdown file 
    """
    with open(f"data/markdown/{namefile}.md", "r", encoding="utf8") as file_to_read:
        text = file_to_read.read()
    return text

class Config(TypedDict):
    """
        Class to easy access configs values
    """
    token: str
    dev_group_chatid: int
    admin_group: int

# config
with open('config/settings.yaml', 'r', encoding='utf-8') as yaml_config:
    config_map: Config = yaml.load(yaml_config, Loader=yaml.SafeLoader)  # type: ignore

