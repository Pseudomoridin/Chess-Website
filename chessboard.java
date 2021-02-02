int ascii_lowercase = "abcdefghijklmnopqrstuvwxyz"
class chessboard()
{
  private Object[][] populate(Object[][] arr)
  {
    arr[0][0] = new rook("white", [0,0]);
    arr[0][1] = new knight("white", [0,1]);
    arr[0][2] = new bishop("white", [0,2]);
    arr[0][3] = new queen("white", [0,3]);
    arr[0][4] = new king("white", [0,4]);
    arr[0][5] = new bishop("white", [0,5]);
    arr[0][6] = new knight("white", [0,6]);
    arr[0][7] = new rook("white", [0,7]);
    for (int i = 0; i < 8; i++)
    {
      arr[1][i] = new pawn("white", [1,i]);
    }
    for (int i = 0; i < 8; i++)
    {
      arr[6][i] = new pawn("black", [6,i]);
    }
    arr[7][0] = new rook("black", [7,0]);
    arr[7][1] = new knight("black", [7,1]);
    arr[7][2] = new bishop("black", [7,2]);
    arr[7][3] = new queen("black", [7,3]);
    arr[7][4] = new king("black", [7,4]);
    arr[7][5] = new bishop("black", [7,5]);
    arr[7][6] = new knight("black", [7,6]);
    arr[7][7] = new rook("black", [7,7]);
    return arr;
  }
  
  public chessboard()
  {
    private Object[][] this.chessboard = new Object[8][8];
    this.chessboard.populate();
  }

  public move()
  {
    piece.move
  }
}