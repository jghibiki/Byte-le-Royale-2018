# Running The Game

Basic flow of how a game works:
1. A game map is generated.
2. Start a server
3. Start a client. Your client will connect to the server. 
4. The server then orchestrates the game based on the ```game_data.json``` file and responses from the client. The server also generates a ```game_log/``` directory which contains the game log which is used by the visualizer to visualize the game after it has finished running.
5. Wait for the client and server to finish running.
6. Run the visualizer to visualize how the game played out.

***Note: All of the following commands must be run from the root of the repository.***

## Generate a Game Map
Generates a game map ```game_data.json``` file. This file outlines a randomly generated game map.

```shell
python -m game.scripts.generate
```

## Easy Run Script
***Only works for Linux***

Runs both the client and server.
```shell
./run.sh
```

## Run Server
Runs the game server. 

```shell
python -m game.scripts.server
```

## Run Client
Runs the default client (```custom_client.py```).

```shell
python -m game.scripts.client
```

Run a custom client defined in the root of the repository (e.g. ```demo_client.py```). Note that you do not include the ```.py```.

```shell
python -m game.scripts.client --client demo_client
```

#### Run Visualizer

Run the visualizer in `game_log/`

```shell
python -m game.scripts.visualizer
```

Run the visualizer and visualize a different game log.

```shell
python -m game.scripts.visualizer --game-log copied_game_log_path
```

To adjust the brightness of the game (and possibly throw off the colors of your monitor - restart should fix) try adding ```--gamma 1.1```. ```1.0``` should be the default display colorization. Less than ```1.0``` wil make the display darker, greater than ```1.0``` will make the display brighter. ```2.0``` Does some interesting things.
