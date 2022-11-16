"""Constants and common functions"""
import logging
import yaml
from typing import TypedDict

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

class Config(TypedDict):
    token: str
    dev_group_chatid: int
    admin_group: int

# config
with open('config/settings.yaml', 'r', encoding='utf-8') as yaml_config:
    config_map: Config = yaml.load(yaml_config, Loader=yaml.SafeLoader)  # type: ignore
