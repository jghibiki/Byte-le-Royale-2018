# Mini-MechMania-2017-2018
Now with or without nuts. (Advertised as seen)


# Documentation

The documentation for the competition can be found on the [Documentation Website](https://jghibiki.github.io/Mini-MechMania-2017-2018/)

# Scripts

## Shell Scripts

### Run Game
```shell
$ ./run.sh
```

## Python Scripts

### Generate Game
```shell
$ python -m game.scripts.load
```

### Run Terminal Simulation
```shell
$ python -m game.scripts.sim
```

### Visualize Generated Game
```shell
$ python -m game.scripts.load
```

### Run Server
```shell
$ python -m game.scripts.server
```

### Run Client 
```shell
$ python -m game.scripts.client
```

# Visualisation Examples
Maps are read from top to bottom. Both examples show a 2-level game, longer games are supported but become more difficult to render in a terminal.

## Abbreviated Node IDs
             3af0e      
               |
         +------------+
         |            |
       85617        ced2d
         |            |
         +----+ +-----+
         |    | |     |
       946a0 c82d2  0d6d1
         |    | |     |
         +----+ +-----+
         |            |
       a773b        a72f4
         |            |
         +-----+------+
               |       
             d3e80      
               |
         +------------+
         |            |
       536d3        f59f8
         |            |
         +----+ +-----+
         |    | |     |
       9599a acf3e  41ba0
         |    | |     |
         +----+ +-----+
         |            |
       fe636        2c830
         |            |
         +----+ +-----+
         |    | |     |
       849ab 99ef8  ec866
         |    | |     |
         +----+ +-----+
         |            |
       f4520        81a59
         |            |
         +-----+------+
               |       
             bd2e4      


## Trap Type Keys
        T = trap
        M = monster
        R = town/rest
        
                o        
                |
          +------------+
          |            |
          T            T  
          |            |
          +----+ +-----+
          |    | |     |
          T     T      T  
          |    | |     |
          +----+ +-----+
          |            |
          M            T  
          |            |
          +-----+------+
                |       
                R        
                |
          +------------+
          |            |
          T            M  
          |            |
          +----+ +-----+
          |    | |     |
          M     T      M  
          |    | |     |
          +----+ +-----+
          |            |
          M            M  
          |            |
          +----+ +-----+
          |    | |     |
          M     T      T  
          |    | |     |
          +----+ +-----+
          |            |
          M            T  
          |            |
          +-----+------+
                |       
                R        
