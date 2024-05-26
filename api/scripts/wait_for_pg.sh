#!/usr/bin/env bash

sleep 5
  
until PGPASSWORD=$POSTGRES_PASSWORD psql -h "$POSTGRES_HOST" -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c '\q'; do
  echo "Postgres is unavailable"
  sleep 3
done
  
echo "Postgres is ready"
exec "$@"