from curses.textpad import rectangle

import data
from data import (Price, Rectangle, Point, Book, Circle, Employee)
import hw1
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_vowel_count(self):
        x = "hello"
        result = hw1.vowel_count(x)
        expected = 2
        self.assertEqual(expected, result)

    def test_vowel_count(self):
        x = "orange"
        result = hw1.vowel_count(x)
        expected = 3
        self.assertEqual(expected, result)


    # Part 2
    def test_short_lists(self):
        x=[[2,3], [4,6,7], [4], [9,7]]
        result = hw1.short_lists(x)
        expected = [[2,3], [9, 7]]
        self.assertEqual(expected, result)

    def test_short_lists(self):
        x=[[5], [4,0], [5,9,0,0], [9]]
        result = hw1.short_lists(x)
        expected = [[4,0]]
        self.assertEqual(expected, result)

    # Part 3
    def test_ascending_pairs(self):
        x=[[9,6], [5,6,1], [4], [9,7]]
        result = hw1.ascending_pairs(x)
        expected = [[6,9], [5,6,1], [4], [7,9]]
        self.assertEqual(expected, result)

    def test_ascending_pairs(self):
        x=[[10,1], [7,8], [0,0], [11,12]]
        result = hw1.ascending_pairs(x)
        expected = [[1,10], [7,8], [0,0], [11,12]]
        self.assertEqual(expected, result)


    # Part 4
    def test_add_prices(self):
        result = hw1.add_prices(Price(2, 68), Price(3,61))
        expected = 6.29
        self.assertEqual(expected, result)

    def test_add_prices(self):
        result = hw1.add_prices(Price(10, 1), Price(3,2))
        expected = 13.03
        self.assertEqual(expected, result)

    # Part 5
    def test_rectangle_area(self):
        top_left = Point(1,9)
        bottom_right = Point(9,3)
        result = hw1.rectangle_area(Rectangle(top_left, bottom_right))
        expected = 48.0
        self.assertEqual(expected, result)

    def test_rectangle_area(self):
        top_left = Point(10, 21)
        bottom_right = Point(5, 16)
        result = hw1.rectangle_area(Rectangle(top_left, bottom_right))
        expected = -25
        self.assertEqual(expected, result)


    # Part 6
    def test_books_by_author(self):
        author = "Rick Riordan"
        book1 = Book(["Rick Riordan"] , "The lightning Thief")
        book2 = Book(["George Orwell"], "Animal Farm")
        books = [book1, book2]
        result = hw1.books_by_author(author, books)
        expected = [book1]
        self.assertEqual(expected, result)

    def test_books_by_author(self):
        author = "George Orwell"
        book1 = Book(["Rick Riordan"], "The lightning Thief")
        book2 = Book(["George Orwell"], "Animal Farm")
        books = [book1, book2]
        result = hw1.books_by_author(author, books)
        expected = [book2]
        self.assertEqual(expected, result)

    # Part 7
    def test_circle_bound(self):
        top_left = Point(50,20)
        bottom_right = Point(30,10)
        result = hw1.circle_bound(Rectangle(top_left, bottom_right))
        expected = Circle(Point(10.0, 5.0), 42.72001872658765)
        self.assertEqual(expected, result)

    def test_circle_bound(self):
        top_left = Point(10, 50)
        bottom_right = Point(70, 20)
        result = hw1.circle_bound(Rectangle(top_left, bottom_right))
        expected = Circle(Point(-30, 15), 53.150729063673246)
        self.assertEqual(expected, result)
    # Part 8
    def test_below_pay_average(self):
        Employee1 = Employee("Bob", 50)
        Employee2 = Employee("John", 25)
        Employee3 = Employee("Rob", 10)
        list_names = [Employee1, Employee2, Employee3]
        result = hw1.below_pay_average(list_names)
        expected = [Employee2.name, Employee3.name]
        self.assertEqual(expected, result)

    def test_below_pay_average(self):
        Employee1 = Employee("Bob", 0)
        Employee2 = Employee("John", 0)
        Employee3 = Employee("Rob", 0)
        list_names = [Employee1, Employee2, Employee3]
        result = hw1.below_pay_average(list_names)
        expected = []
        self.assertEqual(expected, result)




if __name__ == '__main__':
    unittest.main()
