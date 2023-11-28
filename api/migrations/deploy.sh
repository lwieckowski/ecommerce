#!/bin/bash
set -e

# Wait for PostgreSQL to be ready
until pg_isready -h $DB_HOST -p $DB_PORT -U $DB_USER; do
  echo "Waiting for PostgreSQL to be ready..."
  sleep 1
done

# Run the CMD from the Dockerfile
exec "$@"
