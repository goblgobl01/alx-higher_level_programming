#!/usr/bin/python3
"""rectangle python module."""
from models.base import Base


class Rectangle(Base):
    """a class that define a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor."""
        super().__init__(id)
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Get/set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get the x private attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """set the x private attributes"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """get the private attributes y."""
        return self.__y

    @y.setter
    def y(self, value):
        """set the private attributes y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return the area of the rectangle."""
        return self.__width * self.__height

    def display(self):
        """print representation of the rectangle to the stdout."""
        list = ""
        if self.__y != 0:
            list = list + ("\n" * self.__y)
        for i in range(self.__height):
            if self.__x != 0:
                list = list + (" " * self.__x)
            for j in range(self.__width):
                list = list + "#"
            list = list + "\n"
        print(list[:-1])

    def __str__(self):
        """return a simple string."""
        return (
            f"[Rectangle] ({self.id}) "
            f"{self.__x}/{self.__y} - "
            f"{self.__width}/{self.__height}"
        )
