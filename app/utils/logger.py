# app/utils/logger.py
from loguru import logger


def configure_logger():
    # Remove the existing handlers
    logger.remove()

    # Configure the logger to log to the console
    logger.add(
        "logs/app.log",
        level="DEBUG",
        rotation="1 MB",
        compression="zip",
        format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {module}:{line} - {message}",
        enqueue=True,
        backtrace=True,
        diagnose=True,
    )

    # Log to the console as well
    console_handler = logger.add(
        lambda msg: msg,
        level="DEBUG",
        format="<level>{level}</level> <green>{time:YYYY-MM-DD HH:mm:ss}</green> | <cyan>{module}:{line}</cyan> - <level>{message}</level>",
        enqueue=True,
    )

    return logger
