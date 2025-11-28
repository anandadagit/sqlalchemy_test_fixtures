from models import Owner, Car


def test_owner_str():
    o = Owner(name="Alice")
    assert str(o) == "Alice"


def test_car_str_contains_fields():
    # create a Car instance without DB involvement
    c = Car(id=1, model="ModelX", year=2020, colour="red", owner_id=None, owner=None)
    s = str(c)
    assert "ModelX" in s
    assert "2020" in s
