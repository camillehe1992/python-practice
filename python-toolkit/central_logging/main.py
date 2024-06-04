from log import init_logging
import random

LOG = init_logging()


def generate_random_str(min_count=10, max_count=16):
    return "".join(
        random.sample(
            "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*",
            random.randint(min_count, max_count),
        )
    )


def log_in_regex_patterns_in_string():
    test_case = (
        "John [513-84-7329] made a payment with credit card 1234-5678-9012-3456."
    )
    print(
        f"\n------------------ log_in_regex_patterns_in_string ------------------------ "
    )
    LOG.debug(f"use f-string: {test_case}")
    LOG.debug("use str.format: {}".format(test_case))
    LOG.debug("use string modulo method: %s" % (test_case))
    LOG.debug("use multi string modulo method: %s %s" % (test_case, test_case))
    print(f"the original test_case {test_case}")
    print(f"\n------------------------------------------ ")


def log_in_regex_patterns_in_dict():

    test_case = (
        "John [513-84-7329] made a payment with credit card 1234-5678-9012-3456."
    )

    test_case2 = {
        "user": "John",
        "ssn": "513-84-7329",
        "event": "made a payment with credit card 1234-5678-9012-3456",
    }

    print(
        f"\n--------------------- log_in_regex_patterns_in_dict --------------------- "
    )
    LOG.debug(f"use f-string: {test_case2}")
    LOG.debug("use str.format: {}".format(test_case2))
    LOG.debug("use string modulo method: %s" % (test_case2))
    LOG.debug("use multi string modulo method: %s %s" % (test_case, test_case2))
    print(f"the original test_case {test_case}")
    print(f"\n------------------------------------------ ")


def log_in_args():
    test_case = {"username": "John Doe", "password": generate_random_str()}

    print(f"\n---------------------- log_in_args -------------------- ")
    LOG.debug("use string modulo method: %s" % test_case)
    LOG.debug("use args: %s", test_case)
    LOG.debug("use multi string modulo method: %s %s" % (test_case, test_case))
    LOG.debug("use multi args: %s %s", test_case, test_case)
    print(f"the original test_case {test_case}")
    print(f"\n------------------------------------------ ")


if __name__ == "__main__":
    log_in_regex_patterns_in_string()
    log_in_regex_patterns_in_dict()
    log_in_args()
