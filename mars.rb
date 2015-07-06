class Mars
  
  def initialize(x,y)
    @limitX = x.to_i
    @limitY = y.to_i
    @scents = []
  end
  
  def add(x,y)
    @scents << [x,y]
  end
  
  def includes(x,y)
    # puts "Looking for " + x.to_s + " " + y.to_s + " in " + @scents.to_s
    # puts @scents.include?([x,y])
    @scents.include?([x,y])
  end
  
  attr_reader :limitX, :limitY
  
end


    
