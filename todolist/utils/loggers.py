import logging

"""
This module contains the loggers used in the application.
"""

# Logger's creation for debug
debug_logger = logging.getLogger('debug_logger')
debug_logger.setLevel(logging.DEBUG)
debug_file_handler = logging.FileHandler('logs/debug.log', encoding='utf-8')
debug_formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
debug_file_handler.setFormatter(debug_formatter)
debug_logger.addHandler(debug_file_handler)

# Logger's creation for general
general_logger = logging.getLogger('general_logger')
general_logger.setLevel(logging.INFO)
general_file_handler = logging.FileHandler(
    'logs/general.log', encoding='utf-8')
general_formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
general_file_handler.setFormatter(general_formatter)
general_logger.addHandler(general_file_handler)
