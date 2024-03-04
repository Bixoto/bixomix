import sqlalchemy
from sqlalchemy import Boolean
from sqlalchemy.orm import mapped_column, Mapped


class EnabledMixin:
    """Mixin that adds a boolean 'enabled' field that defaults to ``true``."""
    enabled: Mapped[bool] = mapped_column(Boolean, nullable=False, server_default=sqlalchemy.true())


class EnabledNoMixin:
    """Mixin that adds a boolean 'enabled' field that defaults to ``false``."""
    enabled: Mapped[bool] = mapped_column(Boolean, nullable=False, server_default=sqlalchemy.false())
