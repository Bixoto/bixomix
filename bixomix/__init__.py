from typing import Any, Mapping
from warnings import warn

from sqlalchemy import func

from .dates import CreatedAtMixin, UpdatedAtMixin, CreatedUpdatedAtMixin
from .states import EnabledMixin, EnabledNoMixin

__version__ = "0.1.2"
__all__ = [
    'CreatedAtMixin', 'UpdatedAtMixin', 'CreatedUpdatedAtMixin',
    'EnabledMixin', 'EnabledNoMixin',
    'UpdateFromDictMixin',
]


class UpdateFromDictMixin:
    def update_from_dict(self, updates: Mapping[str, Any], *, always_set_last_update=False):
        """
        Update the model in-place from a dictionary of attributes.
        If the model has a column named ``<attr>_last_update`` and ``<attr>`` is in the updates dictionary,
        then ``<attr>_last_update`` is set to the current time if the new value is different,
        or if ``always_set_last_update`` is set to ``true``.

        :param updates: dictionary of attributes to update.
          Columns that don't exist on the model are skipped with a warning.
        :param always_set_last_update: force-set ``<attr>_last_update`` even if the new value is the same.
        :return: None
        """

        for k, v in updates.items():
            if not hasattr(self, k):
                warn("update_from_dict called on %r with non-existant attribute %r" % (self, k), RuntimeWarning)
                continue

            existing_value = getattr(self, k)
            setattr(self, k, v)

            if always_set_last_update or v != existing_value:
                last_update_column_name = f"{k}_last_update"
                if hasattr(self, last_update_column_name):
                    setattr(self, last_update_column_name, func.now())
