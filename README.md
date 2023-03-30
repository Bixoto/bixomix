# Bixomix

**bixomix** is a collection of SQLAlchemy mixins.

## Support

* Python 3.9+
* SQLAlchemy 2.0+

## Usage

Add mixins after the `Base` class in each model’s parent classes. The order of the mixins doesn’t matter.

```python
from sqlalchemy.orm import DeclarativeBase

from bixomix import CreatedAtMixin


class Base(DeclarativeBase):
    pass


class MyModel(Base, CreatedAtMixin):
    # Add your own fields here
    ...
```

## Mixins

* `CreatedAtMixin`: add a `created_at` datetime field that’s automatically filled with the record’s creation date
* `UpdatedAtMixin`: add an `updated_at` datetime field that’s automatically filled with the record’s last update date
* `CreatedUpdatedAtMixin`: combined version of the previous two mixins