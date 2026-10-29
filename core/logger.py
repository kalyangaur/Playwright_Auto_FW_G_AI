import logging
import sys
from pathlib import Path


def setup_logger():
    log_dir = Path("reports/logs")
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / "automation.log"

    app_logger = logging.getLogger("PlaywrightFramework")
    app_logger.setLevel(logging.DEBUG)

    if not app_logger.handlers:
        # Console Handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        console_formatter = logging.Formatter(
            "%(asctime)s | %(levelname)-8s | %(name)s:%(filename)s:%(lineno)d - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        console_handler.setFormatter(console_formatter)
        app_logger.addHandler(console_handler)

        # File Handler
        file_handler = logging.FileHandler(log_file, encoding="utf-8")
        file_handler.setLevel(logging.DEBUG)
        file_formatter = logging.Formatter(
            "%(asctime)s | %(levelname)-8s | %(name)s:%(filename)s:%(lineno)d - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        file_handler.setFormatter(file_formatter)
        app_logger.addHandler(file_handler)

    return app_logger


logger = setup_logger()

