import unittest
from logging import getLogRecordFactory, CRITICAL, WARNING, getLogger

from pytracelog.base import PyTraceLog


class TestPyTraceLog(unittest.TestCase):
    def test_extend_log_record_without_attrs(self):
        """
        Тестирование расширения логера без атрибутов
        """
        PyTraceLog.extend_log_record()

        factory = getLogRecordFactory()
        record = factory('name', 20, 'pathname', 10, 'message', None, None)
        record_dict = record.__dict__
        self.assertNotEqual(record_dict.get('int_test_attr', None), 123)

    def test_extend_log_record__with_kwargs(self):
        """
        Тестирование расширения логера с атрибутами
        """
        int_test_attr, str_test_attr = 1, 'test_message'

        PyTraceLog.extend_log_record(int_test_attr=int_test_attr, str_test_attr=str_test_attr)

        factory = getLogRecordFactory()
        record = factory('name', 20, 'pathname', 10, 'message', None, None)
        record_dict = record.__dict__
        self.assertEqual(record_dict.get('int_test_attr', None), int_test_attr)
        self.assertEqual(record_dict.get('str_test_attr', None), str_test_attr)

    def test_reset_method_resets_root_level_to_warning(self):
        """
        Проверка сброса уровня логирования
        """

        PyTraceLog.init_root_logger(CRITICAL)
        PyTraceLog.reset()
        root_logger = getLogger()
        result = root_logger.level

        self.assertEqual(WARNING, result)

    def test_reset_method_removes_handlers_and_old_factory(self):
        """
        Проверка наличия обработчиков и фабрики
        """
        PyTraceLog.init_root_logger(CRITICAL)
        PyTraceLog.reset()
        root_logger = getLogger()
        self.assertEqual(len(root_logger.handlers), 0)
        self.assertIsNone(PyTraceLog._old_factory)

    def test_init_tracer_logger_no_existing_handler(self):
        """
        Тестирование инициализации системы трассировки без обработчика
        """
        PyTraceLog._handlers = []
        PyTraceLog.init_tracer_logger()

        self.assertEqual(len(PyTraceLog._handlers), 1)