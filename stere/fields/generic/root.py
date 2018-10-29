from ..field import Field


class Root(Field):
    """Convenience Class on top of Field."""
    def find(self):
        return self._element.find()
