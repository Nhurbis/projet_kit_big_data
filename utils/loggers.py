import logging
import os

"""
This module contains the loggers used in the application.
"""

# Path to the logs folder and the log files (errors and debug)
directory_path = os.path.dirname(os.path.abspath(__file__)) 
path_errors = os.path.join(directory_path, "../logs/errors.log")
path_debug = os.path.join(directory_path, "../logs/debug.log")

# Logger's creation for errors
errors_logger = logging.getLogger('errors_logger')
errors_logger.setLevel(logging.ERROR)
try:   
    errors_file_handler = logging.FileHandler(path_errors, encoding='utf-8')
except FileNotFoundError:
    os.mkdir(os.path.join(directory_path, "../logs"))
    errors_file_handler = logging.FileHandler(path_errors, encoding='utf-8')

errors_formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
errors_file_handler.setFormatter(errors_formatter)
errors_logger.addHandler(errors_file_handler)


# Logger's creation for debug
debug_logger = logging.getLogger('debug_logger')
debug_logger.setLevel(logging.INFO)
try:
    debug_file_handler = logging.FileHandler(path_debug, encoding='utf-8')
except FileNotFoundError:
    os.mkdir(os.path.join(directory_path, "../logs"))
    debug_file_handler = logging.FileHandler(path_debug, encoding='utf-8')
    
debug_formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
debug_file_handler.setFormatter(debug_formatter)
debug_logger.addHandler(debug_file_handler)
