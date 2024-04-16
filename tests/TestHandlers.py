import unittest
from unittest.mock import Mock, patch
from logging import ERROR, INFO, LogRecord, CRITICAL
from sys import stdout, stderr

from pytracelog.logging.handlers import StdoutHandler, StderrHandler, TracerHandler


class TestStdoutHandler(unittest.TestCase):

    def test_init_with_default_stream(self):
        """
        Инициализация обработчика потоком по умолчанию
        """
        handler = StdoutHandler()
        self.assertIs(handler.stream, stdout)

    def test_init_with_custom_stream(self):
        """
        Инициализация обработчика собственным потоком
        """
        custom_stream = Mock()

        handler = StdoutHandler(stream=custom_stream)
        self.assertIs(handler.stream, custom_stream)

    def test_error_record_filter(self):
        """
        Тестирование функции для фильтра записи логов
        """
        logger_error = LogRecord(level=ERROR,
                                 msg='test',
                                 args=(),
                                 name='test',
                                 pathname='test path',
                                 lineno=ERROR,
                                 exc_info=(None, None, None))
        logger_info = LogRecord(level=INFO,
                                msg='test',
                                args=(),
                                name='test',
                                pathname='test path',
                                lineno=INFO,
                                exc_info=(None, None, None))

        false_result = StdoutHandler.error_record_filter(logger_error)
        true_result = StdoutHandler.error_record_filter(logger_info)

        self.assertFalse(false_result)
        self.assertTrue(true_result)

class TestStderrHandler(unittest.TestCase):

    def test_init_with_default_stream(self):
        """
        Инициализация обработчика потоком по умолчанию
        """
        handler = StderrHandler()
        self.assertIs(handler.stream, stderr)

    def test_init_with_custom_stream(self):
        """
        Инициализация обработчика собственным потоком
        """
        custom_stream = Mock()

        handler = StdoutHandler(stream=custom_stream)
        self.assertIs(handler.stream, custom_stream)

    def test_error_record_filter(self):
        """
        Тестирование функции для фильтра записи логов
        """
        logger_error = LogRecord(level=INFO,
                                 msg='test',
                                 args=(),
                                 name='test',
                                 pathname='test path',
                                 lineno=INFO,
                                 exc_info=(None, None, None))
        logger_info = LogRecord(level=ERROR,
                                msg='test',
                                args=(),
                                name='test',
                                pathname='test path',
                                lineno=ERROR,
                                exc_info=(None, None, None))

        false_result = StderrHandler.error_record_filter(logger_error)
        true_result = StderrHandler.error_record_filter(logger_info)

        self.assertFalse(false_result)
        self.assertTrue(true_result)

class TestTracerHandler(unittest.TestCase):
    record = None

    def setUp(self):
        self.record = LogRecord(name='name',
                                level=ERROR,
                                pathname='pathname',
                                lineno=1,
                                msg='message',
                                args=(),
                                exc_info=(None, None, None),
                                func='emit')

    def tearDown(self):
        self.record = None


    def test_emit_with_error_record_exception_and_span(self):

        handler = TracerHandler()
        span_mock = Mock()

        with patch('pytracelog.logging.handlers.get_current_span', return_value=span_mock):
            handler.emit(self.record)

        span_mock.set_status.assert_called_once()
        span_mock.add_event.assert_not_called()
        span_mock.record_exception.assert_called_once()

    def test_get_record_attrs(self):

        handler = TracerHandler()

        result = handler.get_record_attrs(self.record)

        self.assertNotIn('msg', result)
        self.assertNotIn('msecs', result)
        self.assertNotIn('relativeCreated', result)
        self.assertNotIn('otelSpanID', result)
        self.assertNotIn('otelTraceID', result)
        self.assertNotIn('otelServiceName', result)
