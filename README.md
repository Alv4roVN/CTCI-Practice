# CTCI Practice

A pytest-based practice repo for Cracking the Coding Interview problems.
Each problem is a stub function that raises `NotImplementedError` —
implement it, then run the tests to check yourself.

## Setup

```
pip install -r requirements.txt
```

## Running tests

```
pytest -v                 # everything
pytest tests/test_day1.py -v   # just one file
pytest -v -m is_unique          # a single problem, by name
```

A test fails loudly (`NotImplementedError`) until you implement the
corresponding function — that's expected and tells you what's left to do.
