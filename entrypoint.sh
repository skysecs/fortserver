#!/bin/bash
#

rm -f /opt/fortserver/tmp/*.pid

case "$1" in
    start|init_db|upgrade_db)
        set -- /opt/fortserver/jms "$@"
        ;;
esac

exec "$@"
