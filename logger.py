# logger.py

import logging

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] [%(levelname)s] %(name)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

log = logging.getLogger("sip_bot")

def log_error(msg, exc=None):
    if exc:
        log.error(f"{msg}: {exc}", exc_info=True)
    else:
        log.error(msg)

def log_startup():
    log.info("\u26a1\ufe0f SIP Management Bot started")

def log_shutdown():
    log.info("\ud83d\uded1 SIP Management Bot stopped")