require('./mars.rb')

class Robot
  
  @is_lost = false
  
  def initialize(x, y, o, m)
    @xCoordinate = x.to_i
    @yCoordinate = y.to_i
    @orientation = o
    @mars = m
  end
  
  def move
    if is_safe and !@is_lost
      case @orientation
      when 'N'
        @yCoordinate += 1
      when 'S'
        @yCoordinate -= 1
      when 'E'
        @xCoordinate += 1
      when 'W'
        @xCoordinate -= 1
      else
        puts 'Error, line 28'
      end
    elsif !@mars.includes(@xCoordinate,@yCoordinate)
      @is_lost = true
      @mars.add(@xCoordinate,@yCoordinate)
    end
  end
  
  def rotate(direction)
    #puts "Rotate is being called with direction " + direction
    case direction
    when 'L'
      case @orientation
      when 'N'
        @orientation = 'W'
      when 'S'
        @orientation = 'E'
      when 'E'
        @orientation = 'N'
      when 'W'
        @orientation = 'S'
      else
        puts 'Error, line 45'
      end
    when 'R'
      case @orientation
      when 'N'
        @orientation = 'E'
      when 'S'
        @orientation = 'W'
      when 'E'
        @orientation = 'S'
      when 'W'
        @orientation = 'N'
      else
        puts 'Error, line 45'
      end
    end
  end
    
  def is_safe
    # puts "Calling is_safe with orientation " + @orientation
    case @orientation
    when 'W'
      return false if @xCoordinate - 1 < 0
    when 'E'
      return false if @xCoordinate + 1 > @mars.limitX
    when 'S'
      return false if @yCoordinate - 1 < 0
    when 'N'
      return false if @yCoordinate + 1 > @mars.limitY
    end
    # puts "This is safe"
    true
  end
  
  def toString
    string = @xCoordinate.to_s + " " + @yCoordinate.to_s + " " + @orientation
    if @is_lost
      string += " LOST \n"
    else
      string += "\n"
    end
    string
  end

end
