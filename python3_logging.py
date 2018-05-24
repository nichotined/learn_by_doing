import logzero
import logging
import os
import datetime
from pythonjsonlogger import jsonlogger

class LoggerHelper():
    def __init__(self):
        pass

    @staticmethod
    def delete_existing_report():
        pass
        json_log = "/tmp/json_log.log"
        try:
            os.remove(json_log)
        except FileNotFoundError as e:
            print(e)

    @staticmethod
    def simple_logger():
        logger1 = logzero.setup_logger(name="simple", logfile="/tmp/simple_logger.log")
        return logger1

    @staticmethod
    def json_logger():
        json_format = LoggerHelper.json_formatter()
        logger1 = logzero.setup_logger(name="json_log", logfile="/tmp/json_log.log", formatter=json_format)
        return logger1

    @staticmethod
    def json_formatter():
        jsonFormat = CustomJsonFormatter('(message) (timestamp) (level)')
        return jsonFormat

class CustomJsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super(CustomJsonFormatter, self).add_fields(log_record, record, message_dict)
        if not log_record.get('timestamp'):
            # this doesn't use record.created, so it is slightly off
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            log_record['timestamp'] = now
        if log_record.get('level'):
            log_record['level'] = log_record['level'].upper()
        else:
            log_record['level'] = record.levelname


logger_helper = LoggerHelper()
json_logger = logger_helper.json_logger()
simple_logger = logger_helper.simple_logger()

json_logger.debug('DEBUG')
json_logger.info('INFO')
json_logger.warning('WARNING')
json_logger.error('ERROR')
json_logger.exception('EXCEPTION')
json_logger.critical('CRITICAL')

simple_logger.debug('DEBUG')
simple_logger.info('INFO')
simple_logger.warning('WARNING')
simple_logger.error('ERROR')
simple_logger.exception('EXCEPTION')
simple_logger.critical('CRITICAL')