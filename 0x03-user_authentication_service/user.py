#!/usr/bin/env python3
"""User Database Model"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class User(Base):
    """
    This class defines all the model of the table User
    """

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)

    def __repr__(self):
        """
        This function return a string
        representation of the class
        """
        # return f'<User: id {self.id} email
        # {self.email} password {self.hashed_password}>'
