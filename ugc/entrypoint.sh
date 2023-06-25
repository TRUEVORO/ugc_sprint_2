#!/bin/sh

echo "Waiting for Kafka to start..."
while ! nc -z "${KAFKA_HOST}" "${KAFKA_PORT}"; do
  sleep 1
done
echo "Kafka has started"

cd src || exit

gunicorn -c gunicorn/gunicorn.py main:app
