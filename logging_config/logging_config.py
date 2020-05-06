from logging.config import dictConfig

logging_config = {
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "[%(asctime)s.%(msecs)03d|%(name)s|%(levelname)s] %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
            "level": "INFO",
            "stream": "ext://sys.stdout",
        },
        "debug_file_handler": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "DEBUG",
            "formatter": "simple",
            "filename": "./.logged_debug.log",
            "maxBytes": 10485760,  # 10MB
            "backupCount": 20,
            "encoding": "utf8",
            "delay": True,
        },
        "info_file_handler": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "INFO",
            "formatter": "simple",
            "filename": "./.logged_info.log",
            "maxBytes": 10485760,  # 10MB
            "backupCount": 20,
            "encoding": "utf8",
            "delay": True,
        },
        "error_file_handler": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "ERROR",
            "formatter": "simple",
            "filename": "./.logged_errors.log",
            "maxBytes": 10485760,  # 10MB
            "backupCount": 20,
            "encoding": "utf8",
            "delay": True,
        },
    },
    "loggers": {
        "anyconfig": {
            "handlers": [
                "console",
                "debug_file_handler",
                "info_file_handler",
                "error_file_handler",
            ],
            "level": "WARNING",
            "propagate": False,
        },
    },
    "root": {
        "handlers": [
            "console",
            "debug_file_handler",
            "info_file_handler",
            "error_file_handler",
        ],
        "level": "DEBUG",
    },
    "version": 1,
}

dictConfig(logging_config)

if __name__ == "__main__":
    from logging import getLogger

    log = getLogger(__name__)
    log.info("# Logging configured.")
