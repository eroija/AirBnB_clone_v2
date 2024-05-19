#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        # for dbstorage
        name = Column(String(128), nullable=False)
        cities = relationship(
                'City',
                backref='states',
                cascade='all, delete-orphan')

    else:
        name = ""

        # for file storage
        @property
        def cities(self):
            """
            Getter attribute for cities
            """
            from models import storage
            city_list = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
