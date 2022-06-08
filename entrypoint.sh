#!/bin/bash
set -e

python manage.py migrate

# Then exec the container's main process (what's set as CMD in the Dockerfile).
exec "$@"
