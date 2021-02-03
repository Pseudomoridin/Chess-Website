int ascii_lowercase = "abcdefghijklmnopqrstuvwxyz"
class queen()
{
  public queen(string colour, int[] position)
  {
    private string this.colour = colour;
    private int[] this.position = position;
  }

  public void setColour(newColour){this.colour = newColour;}

  public void setPosition(newPos){this.position = newPos;}

  public string getColour(){return this.colour;}

  public int[] getPosition(){return this.position;}

  private boolean move_logic()
  {}

  private boolean move(int[] move)
  {
    if (this.move_logic(move) == true)
    {
      try 
      {
        chessboard[move[0]][move[1]] = this;
        this.setPosition(move);
        return true;
      }
      catch (Exception e)
      {
        return false;
      }
    }
    else
    {
      return false;
    }
  }
}