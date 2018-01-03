#!/bin/bash

if [ -z $1 ]; then
    port_no=8080
else
    port_no=$1
fi

echo "Port number: $port_no";


# trap ctrl-c and call ctrl_c()
trap ctrl_c INT

function ctrl_c() {
    kill $p1;
    kill $p2;
}

echo "Starting Server..."
python -m game.scripts.server --port $port_no &
p1=$!

sleep 6;

echo "Starting Client..."
python -m game.scripts.client --port $port_no &
p2=$!

wait $p1 $p2;
exit;
