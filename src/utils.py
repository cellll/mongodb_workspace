import os
import configparser
# logger
import logging
from logging.handlers import TimedRotatingFileHandler

def get_basic_logger(log_level=logging.INFO):
    logger = logging.getLogger()
    logger_format = '[%(levelname)s] [%(asctime)s] [%(module)s:%(funcName)15s():%(lineno)d] %(message)s'
    logging.basicConfig(format=logger_format)
    logger.setLevel(log_level)
    return logger

def get_timerotatingfile_logger(log_filename:str, log_path:str='', when:str='midnight', interval:int=1, backupCount:int=5, logger_name='', log_level=logging.INFO):
    if not log_path:
        base_path = os.path.dirname(os.path.realpath(__file__))
        base_path = os.path.dirname(base_path)
        log_dirpath = os.path.join(base_path, 'logs')
        if not os.path.exists(log_dirpath):
            os.makedirs(log_dirpath)
        log_path= os.path.join(log_dirpath, log_filename)
        
    logger = logging.getLogger(logger_name)
    logger.setLevel(log_level)
    log_handler = TimedRotatingFileHandler(log_path, when=when, interval=interval, backupCount=backupCount)
    log_formatter = logging.Formatter('[%(levelname)s] [%(asctime)s] [%(module)s:%(funcName)s():%(lineno)d] %(message)s')
    log_handler.setFormatter(log_formatter)
    logger.addHandler(log_handler)
    logger.info(f'[LOG PATH] : {log_path}')
    return logger


def get_db_cfg():
    dirpath = os.path.dirname(os.path.realpath(__file__))
    cfg_filepath = os.path.join(dirpath, 'db.cfg')
    cfg = configparser.ConfigParser()
    cfg.read(cfg_filepath)
    return cfg

def get_db_cfg_dict():
    cfg = get_db_cfg()
    cfg_dict = dict()
    for section in cfg.sections():
        if section not in cfg_dict:
            cfg_dict[section] = dict()
        for key, value in cfg.items(section):
            cfg_dict[section][key] = value
    return cfg_dict
    
def get_db_url():
    cfg = get_db_cfg()
    return cfg.get('mongodb', 'url')

def get_default_db_configs():
    cfg_dict = get_db_cfg_dict()
    return cfg_dict['config']
    