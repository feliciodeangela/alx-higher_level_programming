#!/usr/bin/python3
"""Module containing City class"""
from model_state import Base, State
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class City(Base):
    """Class definition of a City"""
    __tablename__ = 'cities'
    id = Column(
        Integer,
        unique=True,
        autoincrement=True,
        nullable=False,
        primary_key=True
    )
    name = Column(
        String(128),
        nullable=False
    )
    state_id = Column(
        Integer,
        ForeignKey("states.id"),
        nullable=False
    )
