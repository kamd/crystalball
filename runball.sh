#!/bin/bash
pushd ~/code/crystalball
source flaskenv/bin/activate
python index.py
popd
exit 0

