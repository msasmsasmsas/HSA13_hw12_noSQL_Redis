#!/bin/bash
set -e

siege -c 1 -r 10 -H "Content-Type: application/json" -f ./urls_rabbitmq.txt -b