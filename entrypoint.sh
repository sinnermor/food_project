#!/bin/sh

run_tests() {
    pytest -p no:warnings
}

run() {
    python run.py
}

"$@"
