from dataclasses import dataclass
from datetime import datetime

import pytest
from sqlalchemy.sql.functions import now as sql_now

from bixomix import UpdateFromDictMixin


@dataclass
class FakeModel(UpdateFromDictMixin):
    foo: str = "foo"
    bar: str = "bar"


def test_update_from_dict():
    m = FakeModel()
    m.update_from_dict({"foo": "bar"})
    assert m.foo == "bar"


@pytest.mark.filterwarnings("ignore:.*non-existant attribute.*")
def test_update_from_dict_unknown_field():
    m = FakeModel()
    m.update_from_dict({"qux": 42})
    assert not hasattr(m, "qux")


def test_update_from_dict_last_update():
    @dataclass
    class MyFakeModel(UpdateFromDictMixin):
        foo: int
        foo_last_update: datetime

    before = datetime(2010, 1, 1, 0, 0, 0)

    m = MyFakeModel(foo=42, foo_last_update=before)
    m.update_from_dict({})
    assert m.foo_last_update == before

    m.update_from_dict({"foo": 42})
    assert m.foo_last_update == before

    m.update_from_dict({"foo": 43})
    assert isinstance(m.foo_last_update, sql_now)
