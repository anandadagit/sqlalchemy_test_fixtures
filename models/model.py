from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import create_engine

connection_string = "sqlite:///car_owner.db"
engine = create_engine(connection_string, echo=True)

class Base(DeclarativeBase):
    pass

class Owner(Base):
    __tablename__ = "owner"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)

    #one-to-many relationship
    cars: Mapped[list["Car"]] = relationship(
        back_populates="owner", # link to Car.owner
        cascade="all, delete-orphan"
    )

    def __str__(self) -> str:
        return self.name


class Car(Base):
    __tablename__ = "car"
    id: Mapped[int] = mapped_column(primary_key=True)
    model: Mapped[str] = mapped_column(String(30), nullable=False)
    year: Mapped[int] = mapped_column(nullable=False)
    colour: Mapped[str | None] = mapped_column(String(30))
    owner_id: Mapped[int] = mapped_column(ForeignKey("owner.id"))

    #link back to Owner
    owner: Mapped["Owner"] = relationship(back_populates="cars") # link to owner.cars

    def __str__(self) -> str:
        return f"{self.id}, {self.model}, {self.year}, {self.colour}, {self.owner_id}, {self.owner}"

Base.metadata.create_all(engine)