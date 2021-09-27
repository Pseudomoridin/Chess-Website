import {chessboard} from './chessboard.js';

function move_logic(classid) {
  return true;
}

function convert_move_toint() {
  var toint = [];
  var intone = [];
  var inttwo = [];
  var charone = move[0].substring(0,1);
  var chartwo = move[1].substring(0,1);
  intone.push(ascii_lowercase.indexOf(charone) + 1);
  intone.push(String(move[0]).substring(1));
  inttwo.push(ascii_lowercase.indexOf(chartwo) + 1);
  inttwo.push(String(move[1]).substring(1));
  toint.push(intone);
  toint.push(inttwo);
  return toint;
}

function do_move() {
  if (move.length >= 2) {
    intmove = convert_move_toint();
    if (move_logic(document.getElementById(move[0]).className, intmove) == true) {
      document.getElementById(move[1]).className = document.getElementById(move[0]).className;
      document.getElementById(move[0]).className = "empty";
    }
    move = [];
  }
}

var chess_board = new chessboard();
var update_loop = setInterval(do_move, 100);
