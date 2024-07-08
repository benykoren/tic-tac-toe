from flask import Flask, request, jsonify, render_template
from flask_socketio import SocketIO, emit, join_room

from business_logic import Game, Player

app = Flask(__name__)
socketio = SocketIO(app)

games = {}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/create', methods=['POST'])
def create_game():
    game = Game()
    games[game.id] = game
    return jsonify({'game_id': game.id})


@app.route('/join', methods=['POST'])
def join_game():
    game_id = request.json.get('game_id')
    if game_id in games:
        game = games[game_id]
        if game.add_player(Player('X' if len(game.players) == 0 else 'O')):
            return jsonify({'success': True, 'game_id': game_id, 'player_symbol': game.players[-1].symbol})
    return jsonify({'success': False, 'error': 'Game full or does not exist'})


@socketio.on('move')
def handle_move(data):
    game_id = data['game_id']
    position = data['position']
    player_symbol = data['player_symbol']

    if game_id in games:
        game = games[game_id]
        if game.current_turn == player_symbol:
            if game.make_move(position, Player(player_symbol)):
                emit('update', {'board': game.board, 'current_turn': game.current_turn, 'winner': game.winner},
                     room=game_id)
            else:
                emit('error', {'message': 'Invalid move'}, room=game_id)
        else:
            emit('error', {'message': 'Not your turn'}, room=game_id)


@socketio.on('join')
def on_join(data):
    game_id = data['game_id']
    join_room(game_id)
    game = games[game_id]
    emit('update', {'board': game.board, 'current_turn': game.current_turn, 'winner': game.winner}, room=game_id)


if __name__ == '__main__':
    socketio.run(app, debug=True, allow_unsafe_werkzeug=True)
