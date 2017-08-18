#!/bin/bash

pkill conky
rm -r ~/.conky > /dev/null 2>&1 || { echo "Error removing directory"; exit 1; }
