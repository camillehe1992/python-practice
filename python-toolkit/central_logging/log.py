import re
import time
import logging
import logging.config

regex_patterns = [
    # U.S. Social Security numbers
    r"\d{3}-\d{2}-\d{4}",
    # Credit card numbers
    r"\d{4}-\d{4}-\d{4}-\d{4}",
]


# mask sensitive data in record.msg
class SensitiveDataFilter1(logging.Filter):
    patterns = regex_patterns

    def filter(self, record):
        record.msg = self.mask_sensitive_data(record.msg)
        return True

    def mask_sensitive_data(self, message):
        for pattern in self.patterns:
            message = re.sub(pattern, "******", message)
        return message


# a list of keys that values are sensitive data in a dict
sensitive_keys = (
    "headers",
    "credentials",
    "Authorization",
    "token",
    "password",
)


# mask sensitive data in dictionary.values() using record.msg
class SensitiveDataFilter2(logging.Filter):
    patterns = regex_patterns
    sensitive_keys = sensitive_keys

    def filter(self, record):
        record.msg = self.mask_sensitive_msg(record.msg)
        return True

    def mask_sensitive_msg(self, message):
        for pattern in self.patterns:
            message = re.sub(pattern, "******", message)

        for key in self.sensitive_keys:
            pattern_str = rf"'{key}': '[^']+'"
            replace = f"'{key}': ******"
            message = re.sub(pattern_str, replace, message)
        return message


# mask sensitive data in dictionary.values() using record.args
class SensitiveDataFilter3(logging.Filter):
    patterns = regex_patterns
    sensitive_keys = sensitive_keys

    def filter(self, record):
        try:
            # print(f"record.msg {record.msg}")
            # print(f"record.args {record.args}")
            record.args = self.mask_sensitive_args(record.args)
            record.msg = self.mask_sensitive_msg(record.msg)
            return True
        except Exception as e:
            pass

    def mask_sensitive_args(self, args):
        if isinstance(args, dict):
            new_args = args.copy()
            for key in args.keys():
                if key in sensitive_keys:
                    new_args[key] = "******"
                else:
                    # mask sensitive data in dict values
                    new_args[key] = self.mask_sensitive_msg(args[key])
            return new_args
        # when there are multi arg in record.args
        return tuple([self.mask_sensitive_msg(arg) for arg in args])

    def mask_sensitive_msg(self, message):
        # mask sensitive data in multi record.args
        if isinstance(message, dict):
            return self.mask_sensitive_args(message)
        if isinstance(message, str):
            for pattern in self.patterns:
                message = re.sub(pattern, "******", message)

            for key in self.sensitive_keys:
                pattern_str = rf"'{key}': '[^']+'"
                replace = f"'{key}': '******'"
                message = re.sub(pattern_str, replace, message)
        return message


def init_logging(
    log_level: str = "DEBUG", formatter: str = "console"
) -> logging.Logger:
    """Returns a pre-configured logger for console output and optional log
    file output.

    Args:
        log_level (str): the target debuging level for logs
        formatter (str): the selected formatter for logs

    Returns:
        logger (object): the logger object
    """

    LOG_CONFIG = {
        "version": 1,
        "handlers": {
            "stdout": {
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
                "formatter": formatter,
                "filters": ["sensitive_data_filter"],
            }
        },
        "filters": {
            "sensitive_data_filter": {
                "()": SensitiveDataFilter3,
            }
        },
        "formatters": {
            "json": {
                "format": (
                    '{"msg":"%(message)s","level":"%(levelname)s",'
                    '"file":"%(filename)s","line":%(lineno)d,'
                    '"module":"%(module)s","func":"%(funcName)s"}'
                ),
                "datefmt": "%Y-%m-%dT%H:%M:%SZ",
            },
            "console": {
                "format": "%(asctime)s %(levelname)s : %(message)s",
                "datefmt": "%Y-%m-%dT%H:%M:%SZ",
            },
        },
        "root": {"handlers": ["stdout"], "level": log_level},
    }

    logging.Formatter.converter = time.gmtime
    logging.config.dictConfig(LOG_CONFIG)

    logger = logging.getLogger(__name__)

    logger.debug("configure logging with loglevel=%s", log_level)

    return logger
