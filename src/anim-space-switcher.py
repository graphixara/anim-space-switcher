import os
import logging
import yaml
# import maya.cmds as cmds

logger = logging.getLogger('anim-space-switcher')
stream = logging.StreamHandler()
formatter    = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
stream.setFormatter(formatter)
logger.addHandler(stream)
logger.setLevel(logging.INFO)

class anim_space_switcher(object):

    def __init__(self):
        """Constructor for Anim Space Swicher class"""
        self.attribute_names = []
        self.read_config()
        logger.info(self.attribute_names[0])

    def read_config(self):
        """Read config file to get attibute names"""
        try:
            current_dir = os.path.dirname(__file__)

            config_file_path = os.path.join(current_dir, 'config', 'settings.yml')

            with open(config_file_path, 'r') as file_object:
                data = yaml.safe_load(file_object)
                self.attribute_names.extend(data['attribute-names'])

        except Exception as e:
            logger.error(e)

x = anim_space_switcher()
