import firebase_admin
from firebase_admin import credentials, db
import os
from dotenv import load_dotenv
from loguru import logger
import sys

load_dotenv()

logger.remove()
logger.add("call_logs.log", level="INFO", colorize=True)

class FirebaseListener:
    def __init__(self, credential_path: str, db_url: str, ref_path: str = 'call_logs'):
        self.credential_path = credential_path
        self.db_url = db_url
        self.ref_path = ref_path
        self._init_firebase()
        self.ref = db.reference(self.ref_path)

    def _init_firebase(self):
        if not firebase_admin._apps:
            cred = credentials.Certificate(self.credential_path)
            firebase_admin.initialize_app(cred, {
                'databaseURL': self.db_url
            })
            logger.info("[Firebase] Firebase bağlantısı başlatıldı.")
        else:
            logger.info("[Firebase] Firebase zaten başlatılmış.")

    def start_listening(self, callback_func):
        logger.info(f"[Dinleyici] Firebase '{self.ref_path}' referansı dinleniyor...")

        def firebase_callback(event):
            if event.event_type == 'put' and event.path != '/':
                logger.info(f"[Dinleyici] Yeni çağrı geldi: {event.data}")
                callback_func(event.data)

        self.ref.listen(firebase_callback)
