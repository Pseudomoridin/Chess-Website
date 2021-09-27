import {bishop} from './chess_pieces_js/bishop.js';
import {empty} from './chess_pieces_js/empty.js';
import {king} from './chess_pieces_js/king.js';
import {knight} from './chess_pieces_js/knight.js';
import {pawn} from './chess_pieces_js/pawn.js';
import {queen} from './chess_pieces_js/queen.js';
import {rook} from './chess_pieces_js/rook.js';

export class chessboard {
  constructor () {
    var a1 = new rook();
    var b1 = new knight();
    var c1 = new bishop();
    var d1 = new queen();
    var e1 = new king();
    var f1 = new bishop();
    var g1 = new knight();
    var h1 = new rook();

    var a2 = new pawn();
    var b2 = new pawn();
    var c2 = new pawn();
    var d2 = new pawn();
    var e2 = new pawn();
    var f2 = new pawn();
    var g2 = new pawn();
    var h2 = new pawn();

    var a3 = new empty();
    var b3 = new empty();
    var c3 = new empty();
    var d3 = new empty();
    var e3 = new empty();
    var f3 = new empty();
    var g3 = new empty();
    var h3 = new empty();
  
    var a4 = null;
    var b4 = null;
    var c4 = null;
    var d4 = null;
    var e4 = null;
    var f4 = null;
    var g4 = null;
    var h4 = null;
  
    var a5 = null;
    var b5 = null;
    var c5 = null;
    var d5 = null;
    var e5 = null;
    var f5 = null;
    var g5 = null;
    var h5 = null;
  
    var a6 = null;
    var b6 = null;
    var c6 = null;
    var d6 = null;
    var e6 = null;
    var f6 = null;
    var g6 = null;
    var h6 = null;
  
    var a7 = new pawn();
    var b7 = new pawn();
    var c7 = new pawn();
    var d7 = new pawn();
    var e7 = new pawn();
    var f7 = new pawn();
    var g7 = new pawn();
    var h7 = new pawn();
  
    var a8 = new rook();
    var b8 = new knight();
    var c8 = new bishop();
    var d8 = new queen();
    var e8 = new king();
    var f8 = new bishop();
    var g8 = new knight();
    var h8 = new rook();

    var chessboard = [
      [a1,b1,c1,d1,e1,f1,g1,h1],
      [a2,b2,c2,d2,e2,f2,g2,h2],
      [a3,b3,c3,d3,e3,f3,g3,h3],
      [a4,b4,c4,d4,e4,f4,g4,h4],
      [a5,b5,c5,d5,e5,f5,g5,h5],
      [a6,b6,c6,d6,e6,f6,g6,h6],
      [a7,b7,c7,d7,e7,f7,g7,h7],
      [a8,b8,c8,d8,e8,f8,g8,h8],
    ];
  }

  get_board() {
    return this.chessboard;
  }

  get_piece(x, y) {
    return chessboard[y][x];
  }
  move_logic(object_class, move) {
    var pos1 = move[0];
    var pos2 = move[1];
  }
}