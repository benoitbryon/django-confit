"""Custom colander nodes."""
from __future__ import absolute_import

import colander


class TupleOrNone(colander.Tuple):
    """A node that can be either a tuple, or ``None``."""
    def _validate(self, node, value):
        """Accept None as a valid value."""
        if value is None:
            return colander.null
        else:
            return super(TupleOrNone, self)._validate(node, value)

    def _impl(self, node, value, callback):
        if value is colander.null or value is None:
            return colander.null
        else:
            return super(TupleOrNone, self)._impl(node, value, callback)
