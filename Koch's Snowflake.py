from graphics import*
import math

win = GraphWin("Koch Snowflake", 300, 400)
win.setBackground("white")
win.setCoords(0, 0, 300, 400)

def koch(window, x1, y1, x2, y2, iteration, angle_type):
    iteration -= 1
    
    if iteration == 0:
        return

    else:
        point_1 = Point(x1, y1)
        point_2 = Point(x2, y2)

        line = Line(point_1, point_2)
        line.draw(window)

        if angle_type == 1:

            length = (x2 - x1)/3
            half = length/2
            triangle_height = math.sqrt((length**2)-(half**2))
        
            x_1 = x1 + length
            y_1 = y1
            
            x_3 = x_1 + length
            y_3 = y1

            x_2 = x_1 + half
            y_2 = y1 + triangle_height
        
            line_point = Point(x_2, y_2)
            line1_point = Point(x_1, y_1)
            line2_point = Point(x_3, y_3)

            erase_line = Line(line1_point, line2_point)
            erase_line.setFill("white")
            erase_line.draw(window)

            line_1 = Line(line1_point, line_point)
            line_2 = Line(line2_point, line_point)
            line_1.draw(window)
            line_2.draw(window)

            koch(window, x1, y1, x_1, y_1, iteration, 1)
            koch(window, x_1, y_1, x_2, y_2, iteration, 4)
            koch(window, x_3, y_3, x_2, y_2, iteration, 5)
            koch(window, x_3, y_3, x2, y2, iteration, 1)

        elif angle_type == 2:

            length = (math.sqrt(((y1 - y2)**2)+((x2-x1)**2)))/3
            half = length/2
            triangle_height = math.sqrt((length**2)-(half**2))
        
            x_1 = x1 + half
            y_1 = y1 - triangle_height
            
            x_3 = x_1 + half
            y_3 = y2 + triangle_height

            x_2 = x1
            y_2 = y_3
        
            line_point = Point(x_2, y_2)
            line1_point = Point(x_1, y_1)
            line2_point = Point(x_3, y_3)

            erase_line = Line(line1_point, line2_point)
            erase_line.setFill("white")
            erase_line.setWidth(3)
            erase_line.draw(window)

            line_1 = Line(line1_point, line_point)
            line_2 = Line(line2_point, line_point)
            line_1.draw(window)
            line_2.draw(window)

            koch(window, x1, y1, x_1, y_1, iteration, 2)
            koch(window, x_2, y_2, x_1, y_1, iteration, 4)
            koch(window, x_2, y_2, x_3, y_3, iteration, 6)
            koch(window, x_3, y_3, x2, y2, iteration, 2)

        elif angle_type == 3:

            length = (math.sqrt(((y1 - y2)**2)+((x1-x2)**2)))/3
            half = length/2
            triangle_height = math.sqrt((length**2)-(half**2))
            
            x_1 = x1 - half
            y_1 = y1 - triangle_height
            
            x_3 = x_1 - half
            y_3 = y2 + triangle_height

            x_2 = x1
            y_2 = y_3
        
            line_point = Point(x_2, y_2)
            line1_point = Point(x_1, y_1)
            line2_point = Point(x_3, y_3)

            erase_line = Line(line1_point, line2_point)
            erase_line.setFill("white")
            erase_line.setWidth(3)
            erase_line.draw(window)

            line_1 = Line(line1_point, line_point)
            line_2 = Line(line2_point, line_point)
            line_1.draw(window)
            line_2.draw(window)

            koch(window, x1, y1, x_1, y_1, iteration, 3)
            koch(window, x_2, y_2, x_1, y_1, iteration, 5)
            koch(window, x_3, y_3, x_2, y_2, iteration, 6)
            koch(window, x_3, y_3, x2, y2, iteration, 3)

        elif angle_type == 4:

            length = (math.sqrt(((y2 - y1)**2)+((x2-x1)**2)))/3
            half = length/2
            triangle_height = math.sqrt((length**2)-(half**2))
            
            x_1 = x1 + half
            y_1 = y1 + triangle_height
            
            x_3 = x_1 + half
            y_3 = y2 - triangle_height
            
            x_2 = x1
            y_2 = y_3
        
            line_point = Point(x_2, y_2)
            line1_point = Point(x_1, y_1)
            line2_point = Point(x_3, y_3)

            erase_line = Line(line1_point, line2_point)
            erase_line.setFill("white")
            erase_line.setWidth(3)
            erase_line.draw(window)

            line_1 = Line(line1_point, line_point)
            line_2 = Line(line2_point, line_point)
            line_1.draw(window)
            line_2.draw(window)

            koch(window, x_3, y_3, x2, y2, iteration, 4)
            koch(window, x_2, y_2, x_3, y_3, iteration, 1)
            koch(window, x_2, y_2, x_1, y_1, iteration, 2)
            koch(window, x1, y1, x_1, y_1, iteration, 4)

        elif angle_type == 5:

            length = (math.sqrt(((y2 - y1)**2)+((x1-x2)**2)))/3
            half = length/2
            triangle_height = math.sqrt((length**2)-(half**2))
            
            x_1 = x1 - half
            y_1 = y1 + triangle_height
            
            x_3 = x_1 - half
            y_3 = y2 - triangle_height

            x_2 = x1
            y_2 = y_3
        
            line_point = Point(x_2, y_2)
            line1_point = Point(x_1, y_1)
            line2_point = Point(x_3, y_3)

            erase_line = Line(line1_point, line2_point)
            erase_line.setFill("white")
            erase_line.setWidth(3)
            erase_line.draw(window)

            line_1 = Line(line1_point, line_point)
            line_2 = Line(line2_point, line_point)
            line_1.draw(window)
            line_2.draw(window)
            
            koch(window, x_3, y_3, x2, y2, iteration, 5)
            koch(window, x_3, y_3, x_2, y_2, iteration, 1)
            koch(window, x_2, y_2, x_1, y_1, iteration, 3)
            koch(window, x1, y1, x_1, y_1, iteration, 5)

        elif angle_type == 6:

            length = (x2 - x1)/3
            half = length/2
            triangle_height = math.sqrt((length**2)-(half**2))
            
            x_1 = x1 + length
            y_1 = y1
            
            x_2 = x_1 + (half)
            y_2 = y1 - triangle_height
            
            x_3 = x_2 + (half)
            y_3 = y1
            
            line_point = Point(x_2, y_2)
            line1_point = Point(x_1, y_1)
            line2_point = Point(x_3, y_3)

            erase_line = Line(line1_point, line2_point)
            erase_line.setFill("white")
            erase_line.draw(window)

            line_1 = Line(line1_point, line_point)
            line_2 = Line(line2_point, line_point)
            line_1.draw(window)
            line_2.draw(window)

            koch(window, x1, y1, x_1, y_1, iteration, 6)
            koch(window, x_1, y_1, x_2, y_2, iteration, 2)
            koch(window, x_3, y_3, x_2, y_2, iteration, 3)
            koch(window, x_3, y_3, x2, y2, iteration, 6)
            

def main():
    iterations = 6
    height = (math.sqrt((260**2)-(130**2)))
    koch(win, 20, 280, 280, 280, iterations, 1)
    koch(win, 20, 280, 150, 280 - height, iterations, 2)
    koch(win, 280, 280, 150, 280 - height, iterations, 3)

main()
