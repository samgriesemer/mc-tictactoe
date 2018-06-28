import json
import os
from flask import Flask, Response, jsonify, request, session, abort

from node import Node
from board import Board
from mc import UCT

app = Flask(__name__)
app.secret_key = 'R\x0f\x9e\x0e+5j\xaa,\x852\xb8\x9f;\x1f\x02\xe1{s\xe7\x94S\xab\x94'

@app.route('/', methods=['GET'])
def run():

  # establish board
  b = Board()
  session['state'] = b.state.tolist()
  session['player'] = 0
  return jsonify(session['state'])

@app.route('/update', methods=['POST'])
def update():

  # get data from post
  data = request.get_json()
  action_type = data['action_type']
  c = None

  # initialize board
  b = Board(session['state'])
  b.player = session['player']

  # test is state is terminal
  if b.get_moves() == [] or b.result():
    return error(400, 'State is terminal.')

  # manual action type
  if action_type == 'm':

    # player move
    a = data['action']
    if not b.move(a): 
      return error(400, 'Invalid action.')

  # automatic action type
  elif action_type == 'a':

    # bot move
    n = UCT(b,250)
    c = n['children']
    b.move(n['action'])

  # test if player who just moved has won
  winner = ""
  if b.result():
    winner = b.player^1

  # update session variables 
  session['state']  = b.state.tolist()
  session['player'] = b.player

  return jsonify({"state":session['state'], "winner":winner, "children":c})

@app.route('/reset', methods=['GET'])
def refresh():
  session.clear()

def error(code, message):
  response = jsonify({'statusText':message})
  response.status_code = code
  return response

if __name__ == '__main__':
  app.run()