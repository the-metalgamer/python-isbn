"""
Classes for ISBN numbers
"""


class ISBN10(object):

    """
    Class for the ISBN10 number
    """

    def __init__(self, isbn):

        """
        Constructor method for the ISBN10 class
        """

        self._isbn = None
        self.isbn = isbn

    def _setisbn(self, isbn):

        """
        Checks if the isbn has an length of 9 or 10 and then sets the _isbn
        attribute to it

        @param isbn: the isbn, must be a string
        """
        if isinstance(isbn, str):
            if len(isbn) in (9, 10):
                self._isbn = isbn
            else:
                raise ValueError("isbn must have an lenght of 9 or 10")
        else:
            raise TypeError("isbn must be a string")

    def _getisbn(self):

        """
        Returns the _isbn attribute
        """

        return self._isbn

    def _delisbn(self):

        """
        Deletes the _isbn attribute
        """

        del self._isbn

    isbn = property(_getisbn, _setisbn, _delisbn)

    def _create_checksum(self, chars):

        """
        Calculates the checksum digit for the isbn

        @param chars: A list of the characters of an isbn, must be a list

        Returns the checksum digit as string
        """

        val = sum((x + 2) * int(y) for x, y in enumerate(reversed(chars)))

        check = 11 - (val % 11)
        if check == 10:
            check = "X"
        elif check == 11:
            check = "0"

        return str(check)

    def validate(self):

        """
        Checks if the isbn checksum digit is correct.
        Returns True if that is the case, else False.
        """

        if len(self.isbn) == 10:
            chars = list(self.isbn)

            last = chars.pop()

            check = self._create_checksum(chars)

            if check == last:
                return True
            else:
                return False
        else:
            raise ValueError("self.isbn must have an length of 10")

    def calculate_checksum(self, force=False):

        """
        Add the checksum digit to the isbn number, if it is not already there.

        @param force: Add the checksum digit, even if it is already there. Must
                      be a boolean.
        """

        if force:
            chars = list(self.isbn)
            chars.pop()
            self.isbn = "".join(chars)

        if len(self.isbn) == 9:
            chars = list(self.isbn)

            check = self._create_checksum(chars)

            chars.append(check)

            self.isbn = "".join(chars)
        else:
            raise ValueError("self.isbn must have an length of 9")

    def converttoISBN13(self):

        """
        Converts the isbn10 to a isbn13 number.

        Returns an instance of the ISBN13 class.
        """

        if len(self.isbn) == 10:
            chars = list(self.isbn)
            chars.pop()
            isbn = "".join(chars)
        else:
            chars = list(self.isbn)
            isbn = "".join(chars)

        isbn = "978" + isbn
        converted = ISBN13(isbn)
        converted.calculate_checksum()

        return converted


class ISBN13(object):

    """
    Class for the ISBN13 number.
    """

    def __init__(self, isbn):

        """
        Constructor method for the ISBN13 class
        """

        self._isbn = None
        self.isbn = isbn

    def _setisbn(self, isbn):

        """
        Checks if the isbn has an length of 12 or 13 and then sets the _isbn
        attribute to it

        @param isbn: the isbn, must be a string
        """

        if isinstance(isbn, str):
            if len(isbn) in (12, 13):
                self._isbn = isbn
            else:
                raise ValueError("isbn must have an lenght of 12 or 13")
        else:
            raise TypeError("isbn must be a string")

    def _getisbn(self):

        """
        Returns the _isbn attribute
        """

        return self._isbn

    def _delisbn(self):

        """
        Deltes the _isbn attribute
        """

        del self._isbn

    isbn = property(_getisbn, _setisbn, _delisbn)

    def _create_checksum(self, chars):

        """
        Calculates the checksum digit for the isbn

        @param chars: A list of the characters of an isbn, must be a list

        Returns the checksum digit as string
        """

        val = sum((x % 2 * 2 + 1) * int(y) for x, y in enumerate(chars))
        check = 10 - (val % 10)

        if check == 10:
            check = "0"

        return str(check)

    def validate(self):

        """
        Checks if the isbn checksum digit is correct.
        Returns True if that is the case, else False.
        """

        if len(self.isbn) == 13:

            chars = list(self.isbn)

            last = chars.pop()

            check = self._create_checksum(chars)

            if check == last:
                return True
            else:
                return False

    def calculate_checksum(self, force=False):

        """
        Add the checksum digit to the isbn number, if it is not already there.

        @param force: Add the checksum digit, even if it is already there. Must
                      be a boolean.
        """

        if force:
            chars = list(self.isbn)
            chars.pop()
            self.isbn = "".join(chars)

        if len(self.isbn) == 12:
            chars = list(self.isbn)
            check = self._create_checksum(chars)
            chars.append(check)
            self.isbn = "".join(chars)
        else:
            raise ValueError("self.isbn must have an length of 12")

    def converttoISBN10(self):

        """
        Converts the isbn13 to a isbn10 number.

        Returns an instance of the ISBN10 class.
        """

        if len(self.isbn) == 13:
            chars = list(self.isbn)
            chars.pop()
            isbn = "".join(chars)
        else:
            chars = list(self.isbn)
            isbn = "".join(chars)

        isbn = isbn[3:]

        converted = ISBN10(isbn)
        converted.calculate_checksum()

        return converted
