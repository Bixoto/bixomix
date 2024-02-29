from datetime import datetime

from sqlalchemy import func, DateTime
from sqlalchemy.orm import mapped_column, Mapped


class CreatedAtMixin:
    """SQLAlchemy mixin to add a `created_at` datetime field to a table."""
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())


class UpdatedAtMixin:
    """
    SQLAlchemy mixin to add an `updated_at` datetime field to a table that’s set to `NOW()` every time the row is updated.
    Note that on Postgres this creates the column but update it only from Python. If you need database-level update, use
    a trigger.
    See https://stackoverflow.com/a/71072370/735926 for a possible solution.
    """
    # NOTE:
    #   server_default= tells the DB the default column value while default= sets the default value at the ORM level.
    #   onupdate= sets the value on record update at the ORM level.
    #   Contrary to what its name suggests, server_onupdates= doesn't tell anything to the DB. It only tells the ORM
    #   what to do when the record is updated, assuming the DB does that update by itself (e.g. via a trigger).
    #   See https://stackoverflow.com/a/33532154/735926.
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())


class CreatedUpdatedAtMixin(CreatedAtMixin, UpdatedAtMixin):
    """SQLAlchemy mixin to add `created_at` and `updated_at` datetime fields to a table."""
