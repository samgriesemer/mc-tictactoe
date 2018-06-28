# Monte Carlo Tic-Tac-Toe

This is a python implementation of the monte carlo tree search algorithm used to learn optimal tic-tac-toe play from scratch. The MCTS 'engine' receives tic-tac-toe board states as input and outputs the best next move to make.

## Demo

You can play against the agent live [here](https://smgr.io/rl/mc).

## Contents

This repo contains both the Flask server API and the client-side interface for playing against the tic-tac-toe bot. The Flask server provides an API which receives a board state via POST request, passes the board through MCTS, and returns the resulting board state back to the client. Each time a user makes a move on the board, Javascript sends this POST request to the server and ultimately displays the bot's move once the request is returned.
