import os
import sys
import logging
import yaml

from PySide2.QtWidgets import QMainWindow, QApplication
from PySide2.QtUiTools import QUiLoader
# import maya.cmds as cmds

logger = logging.getLogger('anim-space-switcher')
stream = logging.StreamHandler()
formatter    = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
stream.setFormatter(formatter)
logger.addHandler(stream)
logger.setLevel(logging.INFO)

current_dir = os.path.dirname(__file__)

class anim_space_switcher(QMainWindow):

    def __init__(self):
        """Constructor for Anim Space Swicher class"""
        super(anim_space_switcher, self).__init__()
        self.attribute_names = []
        self.read_config()
        self.load_ui()
        logger.info(self.attribute_names[0])

    def read_config(self):
        """Read config file to get attibute names"""
        try:

            config_file_path = os.path.join(current_dir, 'config', 'settings.yml')

            with open(config_file_path, 'r') as file_object:
                data = yaml.safe_load(file_object)
                self.attribute_names.extend(data['attribute-names'])

        except Exception as e:
            logger.error(e)

    def load_ui(self):
        ui_file_path = os.path.join(current_dir, 'ui', 'main.ui')
        loader = QUiLoader()
        window = loader.load(ui_file_path, self)
        window.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    x = anim_space_switcher()
    app.exec_()
