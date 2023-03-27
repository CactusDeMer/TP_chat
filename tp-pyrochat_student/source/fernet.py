import os
import logging
import hashlib
import base64
import dearpygui.dearpygui as dpg
from Crypto.Cipher import AES

from chat_client import ChatClient
from generic_callback import GenericCallback
from source.ciphered_gui import CipheredGUI
from cryptography.fernet import Fernet


class FernetGUI(CipheredGUI):
    """
    GUI for a chat client. Secured by William LABBE.
    """

    def run_chat(self, sender, app_data)->None:
        # callback used by the connection windows to start a chat session
        host = dpg.get_value("connection_host")
        port = int(dpg.get_value("connection_port"))
        name = dpg.get_value("connection_name")
        password = dpg.get_value("connection_password")
        self._log.info(f"Connecting {name}@{host}:{port}")
        
        self._key = hashlib.sha256(password.endoce()).digest()
        self._key = base64.b64encode(self._key)

        self._callback = GenericCallback()

        self._client = ChatClient(host, port)
        self._client.start(self._callback)
        self._client.register(name)

        dpg.hide_item("connection_windows")
        dpg.show_item("chat_windows")
        dpg.set_value("screen", "Connecting")


 
    def encrypt(self,text)->None:
        key = Fernet(self._key)
        return key.encrypt(bytes(text,'utf-8'))
    

    def decrypt(self,data)->None:
        data = base64.b64decode(data['data'])
        key = Fernet(self._key)
        return key.decrypt(data).decode()



if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    # instanciate the class, create context and related stuff, run the main loop
    client = FernetGUI()
    client.create()
    client.loop()
