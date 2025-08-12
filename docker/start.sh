#!/bin/sh
# start uvicorn in background
uvicorn backend.main:app --host 0.0.0.0 --port 8000 &
# start nginx in foreground
nginx -g 'daemon off;'