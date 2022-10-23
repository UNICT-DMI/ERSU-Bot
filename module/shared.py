"""Constants and common functions"""
import logging
import yaml

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# config
with open('config/settings.yaml', 'r', encoding='utf-8') as yaml_config:
    config_map: dict = yaml.load(yaml_config, Loader=yaml.SafeLoader)
