#!/bin/bash

mysql -h 0.0.0.0 -u root  -p -e "SELECT version();"
