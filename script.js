import {chessboard} from './chessboard.js';

function do_move() {
  if (move.length >= 2) {
    document.getElementById(move[1]).className = document.getElementById(move[0]).className;
    document.getElementById(move[0]).className = "empty";
    move = [];
  }
}

var chess_board = new chessboard();
var update_loop = setInterval(do_move, 100);