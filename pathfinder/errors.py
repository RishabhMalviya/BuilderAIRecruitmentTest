class BaseError(Exception):
    """Base package error"""


class InvalidInputFormatError(BaseError):
    """Represents an invalid input from input file describing treasure map"""


class ShortestPathNotFoundError(BaseError):
    """Represents that no valid shortest path exists from start point to treasure"""
