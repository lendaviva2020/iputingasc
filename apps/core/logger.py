import logging

core = logging.getLogger("iputingasc.core")


def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(f"iputingasc.{name}")
