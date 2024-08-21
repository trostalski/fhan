import logging
import sys

import structlog


def configure_logging():
    # Common processors
    processors = [
        structlog.contextvars.merge_contextvars,
        structlog.processors.add_log_level,
        structlog.processors.TimeStamper(fmt="iso"),
    ]

    # Configure logging to both file and stdout with colors for development
    file_handler = logging.FileHandler(
        filename="fhan.log",
        mode="a",
    )
    stdout_handler = logging.StreamHandler(sys.stdout)

    handlers = [file_handler, stdout_handler]

    logging.basicConfig(
        format="%(message)s",
        level=logging.INFO,
        handlers=handlers,
    )

    # Use different renderers for file and stdout
    file_processor = structlog.processors.JSONRenderer()
    console_processor = structlog.dev.ConsoleRenderer(colors=True)

    processors.append(structlog.stdlib.ProcessorFormatter.wrap_for_formatter)

    structlog.configure(
        processors=processors,
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )

    # Configure different formatters for file and console output
    file_formatter = structlog.stdlib.ProcessorFormatter(
        processor=file_processor,
    )
    console_formatter = structlog.stdlib.ProcessorFormatter(
        processor=console_processor,
    )

    file_handler.setFormatter(file_formatter)
    # stdout_handler.setFormatter(console_formatter)


# Configure logging based on the settings
configure_logging()

# Get a logger instance
logger: structlog.stdlib.BoundLogger = structlog.get_logger()
