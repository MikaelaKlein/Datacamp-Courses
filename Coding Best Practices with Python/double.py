def double(n: float) -> float:
	"""Multiply a number by 2.
    Arguments:
        n: The number to be doubled.
    Returns:
        The value of n times 2.
    Examples:
        >>> double(2)
        4.0
    """
	if type(n) == float:
		return n * 2
	else:
		raise TypeError

# test_double('2')