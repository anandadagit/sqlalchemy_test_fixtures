from models import Owner, Car


def test_create_owner_and_car(session):
    owner = Owner(name="Bob")
    session.add(owner)
    session.commit()
    assert owner.id is not None

    car = Car(model="Civic", year=2018, colour="blue", owner=owner)
    session.add(car)
    session.commit()

    q_owner = session.query(Owner).filter_by(name="Bob").one()
    assert q_owner.cars[0].model == "Civic"


def test_cascade_delete(session):
    owner = Owner(name="Carl")
    car1 = Car(model="A", year=2010)
    owner.cars.append(car1)
    session.add(owner)
    session.commit()
    oid = owner.id

    session.delete(owner)
    session.commit()

    res = session.query(Car).filter_by(owner_id=oid).all()
    assert res == []
