import math
from curses.textpad import rectangle

import data
from data import (Price, Rectangle, Book, Circle, Point, Employee)

# Write your functions for each part in the space below
# Part 1
def vowel_count(x:str)-> int:
    count = 0
    idx = 0
    vowels = "AaEeIiOoUu"
    while idx < len(x):
        if x[idx] in vowels:
            count += 1
        idx += 1
    return count

#The function's purpose to is find the amount of vowels in a word/string. The input is a string and output is an integer.
#The parameter x:str. The return type is an int which is the number of vowels in the word.

# Part 2
def short_lists(x:list[list[int]]) -> list[list[int]]:
        return [sublist for sublist in x if len(sublist) == 2]

#The function's purpose is to make a list out of the nested lists in the list that have a length of 2. The input is a list and the output is a list
#The parameter is x:list[list[int]] and the return is list[list[int]] which is a list of the nested list that all have a length of 2.

# Part 3
def ascending_pairs(x:list[list[int]]) -> list[list[int]]:
    list = []
    for sublist in x:
        if len(sublist) == 2 and sublist[0]>sublist[1]:
            list.append([sublist[1], sublist[0]])
        else:
            list.append(sublist)
    return list
#The function's purpose is to make a new list where if any of the nested lists have a length of two, elements of that nested list has to be in ascending order.
#The input is a list with nested lists of integers and the output is another list with nested list. The parameter is x:x:list[list[int]].
#The return is list[list[int] which is the new list containing the nested list that have been changed to ascending order if they have a length of 2.

# Part 4
def add_prices(x:Price, y:Price) -> float:
    dollars = x.dollars + y.dollars
    cents = x.cents + y.cents
    if cents > 0:
        return cents/100 + dollars

#The function's purpose is to add two inputs to find the sum but the cents can't go past 99. The input is two integers(prices). The output is a float which is the sum of the two inputs.
#The parameter is x:price, y:price and the return is a float of the sum.

# Part 5
def rectangle_area(rectangle:Rectangle) -> float:
     width = rectangle.bottom_right.x - rectangle.top_left.x
     length = rectangle.top_left.y - rectangle.bottom_right.y
     return width * length

#The function's purpose is to return the area of a rectangle that is properly axis aligned and the vertical sides are parallel to the y-axis.
#The inputs arw two points, the top left and the bottom right. The parameter is rectangle:Rectangle. The return is a float of the area.

# Part 6
def books_by_author(author:str, list_books:list[Book])-> list[Book]:
    books = []
    for book in list_books:
        if author in book.authors:
            books.append(book)
    return books
#The function's purpose is to return a list of all books in the input list written by the author that is specified in the parameter.
#The inputs are the authors' names and the books they wrote. The parameters are author:str, list_books:list[Book]. The return type is list[Book]. This is a list of books that is written by the inputted author.

# Part 7
def circle_bound(rectangle:Rectangle) -> Circle:
    center_point = Point((rectangle.top_left.x - rectangle.bottom_right.x)/2, (rectangle.top_left.y - rectangle.bottom_right.y)/2)
    radius = math.sqrt((((rectangle.top_left.x - rectangle.bottom_right.x)/2) - rectangle.top_left.x)**2  + (((rectangle.top_left.y - rectangle.bottom_right.y)/2) - rectangle.top_left.y)**2)
    return Circle(center_point, radius)

#The function's purpose is to find the center point and radius of the bounding circle. The inputs are the top left and right point of the rectangle the circle bounds.
#The parameter is rectangle:Rectangle. The return type is Circle. The return is the center point and radius of the circle.

# Part 8
def below_pay_average (employees:list[Employee])-> list[str]:
    average_pay = sum(employee.pay_rate for employee in employees )/len(employees)
    below_average = [employee.name for employee in employees if employee.pay_rate < average_pay]
    return below_average
#The function's purpose is to return a list of names that show the employees that are being paid less than average pay of all employees. The input is a employee's name and their pay.
#The output is a list of the employees' names who have a lower pay than the average pay of all the employees.
# The parameter is employees:list[Employee]. The return is a list of names of the employees with a below average pay.



