#!/bin/bash

OPERATION=gunicorn
IP_SCHEDULE=0.0.0.0:8040
WORKER=2
LOGFORMAT="%(t)s %(h)s %(u)s %(r)s %(s)s %(L)s %(l)s %(p)s"
export PYTHONPATH="${PYTHONPATH}:$(pwd)"

exec ${OPERATION} -b ${IP_SCHEDULE} \
                  -w ${WORKER}  \
                  --access-logfile - \
                  --access-logformat "$LOGFORMAT" \
                  --error-logfile - \
                  RandomServer:app