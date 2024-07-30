import logging
from typing import Optional

from utils.config import settings

logging.getLogger('sqlalchemy').setLevel(level=logging.WARNING)

log: Optional[logging.Logger] = None


def config_logging(formatter: str = None, datefmt: str = None, level: str = None, output_filename: str = None) -> None:
    global log
    log_levels = {'info': logging.INFO, 'debug': logging.DEBUG, 'error': logging.ERROR, 'critical': logging.CRITICAL}
    formatter = formatter or '[%(asctime)s | %(levelname)s]: %(message)s'
    datefmt = datefmt or '%d.%m.%Y %H:%M:%S'
    console_out = logging.StreamHandler()
    level = log_levels.get(level, logging.INFO)
    handlers = [console_out]
    if output_filename:
        handlers.append(logging.FileHandler(output_filename))

    logging.basicConfig(handlers=handlers, format=formatter, datefmt=datefmt, level=level)
    log = logging.getLogger()


config_logging(level='info', output_filename=settings.LOG_FILENAME)


def get_log_channel(name: str = None) -> logging.Logger:
    return log.getChild(name) if name else log
