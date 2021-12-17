#!/bin/bash

mysql -h 0.0.0.0 -P 30000 -u root -p -e "SELECT version();"
