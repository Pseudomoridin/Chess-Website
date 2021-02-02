import java.lang.Math;

class bishop()
{
  public bishop(string colour, int[] position)
  {
    private string this.colour = colour;
    private int[] this.position = position;
  }

  public void setColour(newColour){this.colour = newColour;}

  public void setPosition(newPos){this.position = newPos;}

  public string getColour(){return this.colour;}

  public int[] getPosition(){return this.position;}

  private boolean move_logic(int[] move)
  {
    private int this.diff1 = Math.abs(this.position[0] - move[0]);
    private int this.diff2 = Math.abs(this.position[1] - move[1]);
    if (this.diff1 == this.diff2)
    {
      return true;
    }
    else
    {
      return false;
    }
  }

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