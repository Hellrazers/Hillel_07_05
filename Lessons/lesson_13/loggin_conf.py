import logging
import logging.config

logging.config.fileConfig('loggin_conf.ini')

# Використання логера
logger = logging.getLogger('api')
logger_root = logging.getLogger('root')


logger.debug('our massage DEBUG')
logger_root.error('I\'m ROOT LOGGer')
logger.info('our massage INFO')