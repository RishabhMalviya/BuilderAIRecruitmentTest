class BaseError(Exception):
    """Base package error"""


class ShortestPathNotFoundError(BaseError):
    """Represents that no valid shortest path exists from start point to treasure"""
