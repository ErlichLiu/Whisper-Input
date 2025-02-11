import logging
import colorlog
import os
from logging.handlers import RotatingFileHandler

def setup_logger():
    """配置彩色日志"""
    # 创建logs目录
    os.makedirs('logs', exist_ok=True)
    
    # 控制台处理器
    console_handler = colorlog.StreamHandler()
    console_handler.setFormatter(colorlog.ColoredFormatter(
        fmt='%(asctime)s - %(log_color)s%(levelname)-8s%(reset)s - %(message)s',
        datefmt='%H:%M:%S',
        log_colors={
            'DEBUG':    'cyan',
            'INFO':     'green',
            'WARNING': 'yellow',
            'ERROR':   'red',
            'CRITICAL': 'red,bg_white',
        },
        secondary_log_colors={},
        style='%'
    ))
    
    # 文件处理器
    file_handler = RotatingFileHandler(
        'logs/app.log',
        maxBytes=1024*1024,  # 1MB
        backupCount=5,
        encoding='utf-8'
    )
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s'
    ))
    
    logger = colorlog.getLogger(__name__)
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    logger.setLevel(logging.INFO)
    
    # 移除可能存在的默认处理器
    for handler in logger.handlers[:-2]:
        logger.removeHandler(handler)
    
    return logger

logger = setup_logger()
