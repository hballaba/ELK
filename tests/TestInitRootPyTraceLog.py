import unittest
from logging import (
    WARNING,
    ERROR,
    CRITICAL,
    INFO,
    DEBUG,
    NOTSET,
    getLogger
)

from pytracelog.base import PyTraceLog


class TestInitRootPyTraceLog(unittest.TestCase):
    """
    Тесты инициализации PyTraceLog
    """

    def test_init_logger_with_default_value(self):
        """
        Тест инициализации без передачи параметров
        """

        PyTraceLog.init_root_logger()
        root_logger = getLogger()
        self.assertEqual(len(root_logger.handlers), 2)
        self.assertEqual(root_logger.level, WARNING)

    def test_init_logger_with_warning_value(self):
        """
        Тест инициализации c уровнем логирования WARNING
        """
        PyTraceLog.init_root_logger(WARNING)
        root_logger = getLogger()
        self.assertEqual(len(root_logger.handlers), 2)
        self.assertEqual(root_logger.level, WARNING)

    def test_init_logger_with_ERROR_value(self):
        """
        Тест инициализации c уровнем логирования ERROR
        """
        PyTraceLog.init_root_logger(ERROR)
        root_logger = getLogger()
        self.assertEqual(len(root_logger.handlers), 2)
        self.assertEqual(root_logger.level, ERROR)

    def test_init_logger_with_critical_value(self):
        """
        Тест инициализации c уровнем логирования CRITICAL
        """
        PyTraceLog.init_root_logger(CRITICAL)
        root_logger = getLogger()
        self.assertEqual(len(root_logger.handlers), 2)
        self.assertEqual(root_logger.level, CRITICAL)

    def test_init_logger_with_info_value(self):
        """
        Тест инициализации c уровнем логирования INFO
        """
        PyTraceLog.init_root_logger(INFO)
        root_logger = getLogger()
        self.assertEqual(len(root_logger.handlers), 2)
        self.assertEqual(root_logger.level, INFO)

    def test_init_logger_with_debug_value(self):
        """
        Тест инициализации c уровнем логирования DEBUG
        """
        PyTraceLog.init_root_logger(DEBUG)
        root_logger = getLogger()
        self.assertEqual(len(root_logger.handlers), 2)
        self.assertEqual(root_logger.level, DEBUG)

    def test_init_logger_with_notset_value(self):
        """
        Тест инициализации c уровнем логирования NOTSET
        """
        PyTraceLog.init_root_logger(NOTSET)
        root_logger = getLogger()
        self.assertEqual(len(root_logger.handlers), 2)
        self.assertEqual(root_logger.level, NOTSET)

    def tearDown(self):
        PyTraceLog.reset()
