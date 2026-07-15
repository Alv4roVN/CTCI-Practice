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
pytest -v                            # everything
pytest tests/test_binary_search.py -v   # just one category
pytest -v -m is_unique               # a single problem, by name
```

A test fails loudly (`NotImplementedError`) until you implement the
corresponding function — that's expected and tells you what's left to do.

## Timeouts

Every test is capped at 5 seconds (via `pytest-timeout`, configured in
`pytest.ini`), so an infinite loop fails instead of hanging forever. On
Windows a timeout kills the whole run (not just that one test), so if
you suspect a hang, narrow down with `-m <problem_name>` or a single
test file instead of running everything.

## Saving a solution

`solutions/` is gitignored — it's a private snapshot spot, not part of
the tracked practice code. Once a problem passes, save a copy of it
there (mirroring its category path) before resetting the stub back to
`NotImplementedError` to practice it again later:

```
make save FILE=strings_and_hashing/is_unique.py
make save FILE=is_unique   # bare name also works if it's unambiguous
```

## Resetting a problem

`stubs/` holds the pristine `NotImplementedError` version of every
problem. `make reset` copies from there back over the working file,
discarding whatever's currently there — save first if you want to keep
it. It always asks for confirmation before touching anything:

```
make reset TARGET=all                              # every problem
make reset TARGET=strings_and_hashing               # one category
make reset TARGET=strings_and_hashing/is_unique.py  # one problem
make reset TARGET=is_unique                         # bare name also works
```
