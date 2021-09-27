export class queen {
  constructor(colour, position) {
    this.colour = colour;
    this.position = position;
  }
  move_logic(pos1, pos2) {
    var pos1x = pos1[0];
    var pos1y = pos1[1];
    var pos2x = pos2[0];
    var pos2y = pos2[1];
    var xdiff = Math.abs(pos1x - pos2x);
    var ydiff = Math.abs(pos1y - pos2y);
  }
}