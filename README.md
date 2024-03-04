# Bixomix

**bixomix** is a collection of SQLAlchemy mixins.

## Support

* Python 3.9+
* SQLAlchemy 2.0+

## Install

    pip install bixomix

## Usage

Add mixins after the `Base` class in each model’s parent classes. The order of the mixins doesn’t matter.

```python
from sqlalchemy.orm import DeclarativeBase

from bixomix import CreatedAtMixin, EnabledMixin


class Base(DeclarativeBase):
    pass


class MyModel(Base, CreatedAtMixin, EnabledMixin):
    # Add your own fields here
    ...
```

## Mixins

* `CreatedAtMixin`: add a `created_at` datetime field that’s automatically filled with the record’s creation date
* `UpdatedAtMixin`: add an `updated_at` datetime field that’s automatically filled with the record’s last update date.
  Note that on Postgres this is done in Python; for a database-level update you have to [create a trigger](https://stackoverflow.com/a/71072370/735926).
* `CreatedUpdatedAtMixin`: combined version of the previous two mixins
* `EnabledMixin`: add an `enabled` boolean field (default is `true`)
* `EnabledNoMixin`: same as `EnabledMixin`, but the default value is `false`
* `UpdateFromDictMixin`: add an `update_from_dict` method to update a model in-place given a dictionary of attributes
