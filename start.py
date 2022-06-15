import time
from typing import Union

import webview
import logging
import os

from webview import Window

# from src import package_manager
# from src.package_manager import InstallerManager
# from src.package_manager.constants import *

logging.basicConfig(level=logging.INFO)


def init():
    pass
    # TODO: cleanup the directory if exists
    # if not os.path.isdir(DOWNLOADS_DIR):
    #     os.makedirs(DOWNLOADS_DIR)
    # TODO: Create packages.json


class Api:
    def __init__(self):
        self._window = None  # type: Union[Window, None]
        self._original_size = (400, 800)
        # self.manager = InstallerManager(
        #     installers=[
        #         package_manager.seven_zip_installer,
        #         package_manager.miniconda_installer,
        #     ],
        #     root_path="./system/installations/"
        # )

    def is_installed(self) -> bool:
        return False

    def get_actions(self):
        return [
            {
                "id": "python",
                "actions": ["remove", "update"]
            },
            {
                "id": "7-zip",
                "actions": ["install"]
            },
            {
                "id": "miniconda",
                "actions": ["remove"]
            },
        ] * 4

    def check_update(self):
        pass


    def resize(self, height: int):
        width, _ = self._original_size
        self._window.resize(self._window.width, height)

    def select_dir(self) -> str:
        return self._window.create_file_dialog(webview.FOLDER_DIALOG)[0]

    def get_status(self):
        time.sleep(3) # this sleep is here just for design purpose (remove on prod)
        status = self.manager.get_available()
        return status

    def execute_action(self, id: str, action: str):
        result = {
            "status": "OK"
        }
        print(f"Executing {action} on '{id}'")
        time.sleep(2)
        return result

    def set_windows(self, window: Window):
        self._window = window

    def close(self):
        self._window.destroy()


if __name__ == '__main__':
    init()

    api = Api()
    window = webview.create_window("Heights Install System",
                                   url="www/index.html",
                                   height=400,
                                   width=800,
                                   frameless = True,
                                   easy_drag = True,
                                   js_api=api,
                                   resizable=False
                                   )
    api.set_windows(window)
    webview.start(debug=True, http_server=True)
