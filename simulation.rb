require('./robots.rb')
require('./mars.rb')

name_of_file = "./" + ARGV[0] + ".txt"
name_of_output = "./" + ARGV[0] + "_output.txt"

@commands = []

File.open(name_of_file, "r") do |f|
  f.each_line do |line|
    @commands << line
  end
end

mars = Mars.new(@commands[0][0], @commands[0][2])

counter = 0

File.open(name_of_output, "w") do |f|
  for i in 1..@commands.length
    # Create a robot
    if counter==0
      robot = Robot.new(@commands[i][0],@commands[i][2],@commands[i][4],mars)
      # puts "This robot has been created " + robot.toString
    # Operate robot
    elsif counter==1
      for j in 0..@commands[i].length
        print @commands[i][j]
        case @commands[i][j]
        when "F"
          # puts "I'm moving"
          robot.move
        else
          # puts "I'm rotating"
          robot.rotate(@commands[i][j])
        end
      end
      f.write(robot.toString)
    # Empty line
    elsif counter==2
      counter = -1
    end
    counter += 1
  end
end

puts "The results have been saved in a file named " + ARGV[0]+"_output.txt" 
