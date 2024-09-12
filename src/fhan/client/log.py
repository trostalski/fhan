import logging
import sys
from typing import Optional

import structlog


def configure_logging(logging_level: Optional[str] = "INFO"):
    # Common processors
    processors = [
        structlog.contextvars.merge_contextvars,
        structlog.processors.add_log_level,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.stdlib.filter_by_level,  # Add this line
    ]

    # Set logging level
    numeric_level = getattr(logging, logging_level.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError(f"Invalid log level: {logging_level}")

    # Configure root logger
    logging.basicConfig(
        format="%(message)s",
        level=numeric_level,
        handlers=[],  # Remove default handlers
    )

    # Create handlers
    file_handler = logging.FileHandler(filename=".fhan.log", mode="a")
    stdout_handler = logging.StreamHandler(sys.stdout)

    # Set level for both handlers
    file_handler.setLevel(numeric_level)
    stdout_handler.setLevel(numeric_level)

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
    stdout_handler.setFormatter(console_formatter)

    # Add handlers to root logger
    logging.getLogger().addHandler(file_handler)
    logging.getLogger().addHandler(stdout_handler)


# Get a logger instance
logger: structlog.stdlib.BoundLogger = structlog.get_logger()


def set_logging_level(logging_level: str):
    """Set the logging level for the logger."""
    numeric_level = getattr(logging, logging_level.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError(f"Invalid log level: {logging_level}")
    logging.getLogger().setLevel(numeric_level)
    for handler in logging.getLogger().handlers:
        handler.setLevel(numeric_level)


# Initialize logging with default level
configure_logging()
