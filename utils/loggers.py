import logging

"""
This module contains the loggers used in the application.
"""

# Logger's creation for errors
errors_logger = logging.getLogger('errors_logger')
errors_logger.setLevel(logging.errors)
errors_file_handler = logging.FileHandler('logs/errors.log', encoding='utf-8')
errors_formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
errors_file_handler.setFormatter(errors_formatter)
errors_logger.addHandler(errors_file_handler)

# Logger's creation for debug
debug_logger = logging.getLogger('debug_logger')
debug_logger.setLevel(logging.INFO)
debug_file_handler = logging.FileHandler(
    'logs/debug.log', encoding='utf-8')
debug_formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
debug_file_handler.setFormatter(debug_formatter)
debug_logger.addHandler(debug_file_handler)
