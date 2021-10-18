/*
* Classes
*/
class bishop {
  constructor() {
    this.class = "bishop";
  }
  get_class() {return this.class;}
  move_logic(pos1, pos2) {
    alert(pos1, pos2);
    var pos1x = pos1[0];
    var pos1y = pos1[1];
    var pos2x = pos2[0];
    var pos2y = pos2[1];
    var xdiff = Math.abs(pos1x - pos2x);
    var ydiff = Math.abs(pos1y - pos2y);
    if (Math.abs(xdiff) != Math.abs(ydiff)) {
      return false;
    }
    else {
      return true;
    }
  }
}

class empty {
  constructor() {
    this.class = "empty";
  }
  get_class() {return this.class;}
  move_logic(pos1, pos2) {
    return false;
  }
}

class king {
  constructor() {
    this.class = "king";
  }
  get_class() {return this.class;}
  move_logic(pos1, pos2) {
    var pos1x = pos1[0];
    var pos1y = pos1[1];
    var pos2x = pos2[0];
    var pos2y = pos2[1];
    var xdiff = Math.abs(pos1x - pos2x);
    var ydiff = Math.abs(pos1y - pos2y);
    if (Math.abs(xdiff) >= 2 || Math.abs(ydiff) >= 2) {
      return false;
    }
    if (xdiff == 0 && ydiff == 0) {
      return false;
    }
    /*if (/*check collision allies) {
      return true;
    }*/
  }
}

class knight {
  constructor() {
    this.class = "knight";
  }
  get_class() {return this.class;}
  move_logic(pos1, pos2) {
    var pos1x = pos1[0];
    var pos1y = pos1[1];
    var pos2x = pos2[0];
    var pos2y = pos2[1];
    var xdiff = Math.abs(pos1x - pos2x);
    var ydiff = Math.abs(pos1y - pos2y);
  }
}

class pawn {
  constructor() {
    this.class = "pawn";
    this.has_moved = false;
  }
  get_class() {return this.class;}
  move_logic(pos1, pos2) {
    var pos1x = pos1[0];
    var pos1y = pos1[1];
    var pos2x = pos2[0];
    var pos2y = pos2[1];
    var xdiff = Math.abs(pos1x - pos2x);
    var ydiff = Math.abs(pos1y - pos2y);
    if (xdiff != 0 && !(false/*check for taking piece*/)) {
      return false;
    }
    if (Math.abs(ydiff) === 2 && this.has_moved) {
      return false;
    }
    return true;
  }
}

class queen {
  constructor() {
    this.class = queen;
  }
  get_class() {return this.class;}
  move_logic(pos1, pos2) {
    var pos1x = pos1[0];
    var pos1y = pos1[1];
    var pos2x = pos2[0];
    var pos2y = pos2[1];
    var xdiff = Math.abs(pos1x - pos2x);
    var ydiff = Math.abs(pos1y - pos2y);
  }
}

class rook {
  constructor() {
    this.class = "rook";
  }
  get_class() {return this.class;}
  move_logic(pos1, pos2) {
    var pos1x = pos1[0];
    var pos1y = pos1[1];
    var pos2x = pos2[0];
    var pos2y = pos2[1];
    var xdiff = Math.abs(pos1x - pos2x);
    var ydiff = Math.abs(pos1y - pos2y);
  }
}

class chessboard {
  constructor () {
    this.Chessboard = new Array(8).fill(0).map(x => Array(8).fill(0))
    
    this.Chessboard[0][0] = new rook();
    this.Chessboard[1][0] = new knight();
    this.Chessboard[2][0] = new bishop();
    this.Chessboard[3][0] = new queen();
    this.Chessboard[4][0] = new king();
    this.Chessboard[5][0] = new bishop();
    this.Chessboard[6][0] = new knight();
    this.Chessboard[7][0] = new rook();

    this.Chessboard[0][1] = new pawn();
    this.Chessboard[1][1] = new pawn();
    this.Chessboard[2][1] = new pawn();
    this.Chessboard[3][1] = new pawn();
    this.Chessboard[4][1] = new pawn();
    this.Chessboard[5][1] = new pawn();
    this.Chessboard[6][1] = new pawn();
    this.Chessboard[7][1] = new pawn();

    for (var i = 2; i < 6; i++) {
      for (var j = 0; j < 8; j++) {this.Chessboard[j][i] = new empty();}
    }
  
    this.Chessboard[0][6] = new pawn();
    this.Chessboard[1][6] = new pawn();
    this.Chessboard[2][6] = new pawn();
    this.Chessboard[3][6] = new pawn();
    this.Chessboard[4][6] = new pawn();
    this.Chessboard[5][6] = new pawn();
    this.Chessboard[6][6] = new pawn();
    this.Chessboard[7][6] = new pawn();
  
    this.Chessboard[0][7] = new rook();
    this.Chessboard[1][7] = new knight();
    this.Chessboard[2][7] = new bishop();
    this.Chessboard[3][7] = new queen();
    this.Chessboard[4][7] = new king();
    this.Chessboard[5][7] = new bishop();
    this.Chessboard[6][7] = new knight();
    this.Chessboard[7][7] = new rook();
  }

  get_board() {
    return this.Chessboard;
  }

  get_piece(x, y) {return this.Chessboard[y][x];}
  set_piece(x,y,piece){this.Chessboard[y][x] = piece}
  move_logic(intgmove) {
    var pos1 = intgmove[0];
    pos1.forEach(function(part, index) {this[index] -= 1;}, pos1);
    var pos2 = intgmove[1];
    pos2.forEach(function(part, index) {this[index] -= 1;}, pos2);
    return this.get_piece(pos1[1],pos1[0]).move_logic(pos1, pos2)
  }
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

function click_toggle(buttonID) {
  $(document.getElementById(buttonID)).toggleClass("clicked_piece");
}

function do_move() {
  if (move.length >= 2) {
    intmove = convert_move_toint();
    move.forEach(click_toggle)
    if (chess_board.move_logic(intmove) == true) {
      document.getElementById(move[1]).className = document.getElementById(move[0]).className;
      document.getElementById(move[0]).className = "empty";
      alert(chess_board.get_piece(intmove[0][0],intmove[0][1]).get_class())
      alert(chess_board.get_piece(intmove[1][0],intmove[1][1]).get_class())
      // swapping pieces
      chess_board.set_piece(intmove[1][0],intmove[1][1],chess_board.get_piece(intmove[0][0],intmove[0][1]))
      chess_board.set_piece(intmove[0][0],intmove[0][1], new empty())
      alert(chess_board.get_piece(intmove[0][0],intmove[0][1]).get_class())
      alert(intmove[0])
      alert(chess_board.get_piece(intmove[1][0],intmove[1][1]).get_class())
      alert(intmove[1])
    }
    move = [];
  }
}

function test_if_move_valid() {
  if (move.length >= 2) {
    return
  }
}

var ascii_lowercase = "abcdefgh"
var move = [];
var intmove = [];

//alert("Disclaimer: neither the ai nor the game logic have been implemented yet, I\'m working on it.")

function do_on_click(buttonID) {
  move.push(buttonID);
  $(document.getElementById(buttonID)).toggleClass("clicked_piece");
}

var chess_board = new chessboard();

window.addEventListener("DOMContentLoaded", function(){
  var update_loop = setInterval(do_move, 100);
});
