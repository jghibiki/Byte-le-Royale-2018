#!/bin/bash

# trap ctrl-c and call ctrl_c()
trap ctrl_c INT

function ctrl_c() {
    kill $p1;
    kill $p2;
}

echo "Starting Server..."
python -m game.scripts.server &
p1=$!

sleep 1;

echo "Starting Client..."
python -m game.scripts.client &
p2=$!

wait $p1 $p2;
exit;
