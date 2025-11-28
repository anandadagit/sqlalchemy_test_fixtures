from models import Owner, Car


def test_end_to_end(session):
    # create owner and multiple cars
    owner = Owner(name="Dana")
    owner.cars = [Car(model="M1", year=2001), Car(model="M2", year=2002)]
    session.add(owner)
    session.commit()

    loaded = session.get(Owner, owner.id)
    assert len(loaded.cars) == 2

    # update a car property and persist
    loaded.cars[0].colour = "black"
    session.commit()

    updated = session.get(Car, loaded.cars[0].id)
    assert updated.colour == "black"
