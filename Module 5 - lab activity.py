#Idris Awodeji
#07.31.2024

#Problem 1
#prints Hello world a 100 times 
n=100
for index in range (0,100):
    print ('Hello world')



#Problem 2
#list of numbers
numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]

#loop to print each number and its square on a new line
for number in numbers:
    print(number)
    print(number*number)



#Problem 3
import turtle

#gets user input
num_sides = int(input("Enter the number of sides: "))
length_side = int(input("Enter the length of each side: "))
line_color = input("Enter the line color: ")
fill_color = input("Enter the fill color: ")

#creates turtle object
t = turtle.Turtle()

#sets line color and fill color
t.color(line_color)
t.fillcolor(fill_color)

#calculates angle between the sides
angle = 360 / num_sides

#begins filling polygon
t.begin_fill()

#draws polygon
for _ in range(num_sides):
    t.forward(length_side)
    t.right(angle)

#end filling polygon
t.end_fill()


#hides turtle and displays the window
t.hideturtle()
turtle.done()




#Problem 4
#prints divisible by three for multiples of three
#prints divisible by five for multiples of five
#pritns divisible by both for multiples of both three and five
for n in range(1,51):
    if n%3 == 0:
        print('divisble by three')
    elif n%5 == 0:
        print('divisble by five')
    elif n%3 == 0 and n%5 ==0:
        print('divisble by both') 
    else:
        print (n)



#Problem 5
import turtle

def draw_stop_sign():
# Set up the screen
    screen = turtle.Screen()
    screen.bgcolor("white")
    
# Create turtle object
    t = turtle.Turtle()
    t.speed(3)
    
# Set the color for the stop sign
    t.color("black")
    t.fillcolor("red")
    
# Draw the octagon (stop sign)
    t.begin_fill()
    for _ in range(8):
        t.forward(100)
        t.left(45)
    t.end_fill()
    
# Write "STOP" in the center
    t.penup()
    t.goto(+55, +80)  # Adjust position as needed
    t.pendown()
    t.color("white")
    t.write("STOP", align="center", font=("Arial", 60, "bold"))
    
# Hide the turtle and display the window
    t.hideturtle()
    turtle.done()

# Run the function to draw the stop sign
draw_stop_sign()






