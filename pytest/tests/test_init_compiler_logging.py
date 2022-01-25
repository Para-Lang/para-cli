# coding=utf-8
""" Simple testing calling the Para CLI """
from paralang.compiler import ParaCompiler
from paralang.logging import log_msg

from paralang_cli import RUNTIME_COMPILER
from paralang_cli.logging import ParaCLIFileHandler, ParaCLIStreamHandler


class TestCompilerLoggingSetup:
    def test_simple_logger(self):
        compiler = ParaCompiler()
        assert compiler.logger, "Expected initialised logger instance"

    def test_graphical_logger(self):
        compiler = ParaCompiler()
        assert compiler.logger, "Expected initialised logger instance"

        compiler.init_cli_logging()
        assert compiler.logger, "Expected initialised logger instance"
        assert isinstance(
            compiler.stream_handler, ParaCLIStreamHandler
        )
        assert compiler.file_handler is None

    def test_graphical_logger_with_log_file(self):
        compiler = ParaCompiler()
        assert compiler.logger, "Expected initialised logger instance"

        compiler.init_cli_logging("para-test.log")
        assert compiler.logger, "Expected initialised logger instance"
        assert isinstance(
            compiler.stream_handler, ParaCLIStreamHandler
        )
        assert isinstance(
            compiler.file_handler, ParaCLIFileHandler
        )

    def test_log_simple(self):
        compiler = ParaCompiler()
        compiler.init_cli_logging()
        compiler.logger.info("Logging info")

    def test_log_msg_func(self):
        compiler = ParaCompiler()
        compiler.init_cli_logging()
        log_msg("info", "A simple test message")
