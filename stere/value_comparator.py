class ValueComparator:
    """Store a boolean result, along with the expected and actual value.

    For equality checks, the value of `result` will be used.

    This object is used to get more robust reporting from Field.value_contains
    and Field.value_equals when used with assertions.

    Arguments:
        result (bool): The boolean result of the comparison
        expected (object): The expected value
        actual (object): The actual value
    """

    def __init__(
        self,
        result: bool,
        expected: object = None,
        actual: object = None,
    ):
        self.result = result
        self.expected = expected
        self.actual = actual

    def __repr__(self) -> str:
        """Get a useful representation of this object."""
        return str(self)

    def __str__(self) -> str:
        """Get a string representation of this object."""
        rv = (
            f"{self.result}. "
            f"Expected: {self.expected}, Actual: {self.actual}"
        )
        return rv

    def __eq__(self, other: object) -> bool:
        """Check if other equals self.result."""
        if other == self.result:
            return True
        return False

    def __bool__(self) -> bool:
        """Boolean comparison uses self.result."""
        return self.result
