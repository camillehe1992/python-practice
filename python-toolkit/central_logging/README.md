# Mask Sensitive data using Python Built-in Logging Module

This folder contains files for demostrating how to mask sensitive data using Python built-in logging module.

See the blog for the details <https://dev.to/camillehe1992/mask-sensitive-data-using-python-built-in-logging-module-45fa>.

```sh
├── README.md
├── __init__.py
├── log.py          # Define and setup log configuration
└── main.py         # Entry for test cases.
```

There are three Filter classes in `log.py`:

- SensitiveDataFilter1 (Base)
- SensitiveDataFilter2 (Advanced)
- SensitiveDataFilter3 (Default)

You can update the target filter class in **LOG_CONFIG** to use different `filter` in logging. Please be noted, class **SensitiveDataFilter1** cannot mask sensitive data in _record.args_. class **SensitiveDataFilter2** cannot handle multiple args scenarios.

```python
...
"filters": {
    "sensitive_data_filter": {
        "()": SensitiveDataFilter3,
    }
},
...
```
