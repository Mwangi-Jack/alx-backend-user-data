#!/usr/bin/env python3
"""Database  module
"""
from typing import Dict, Any
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import NoResultFound, InvalidRequestError
from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """This method returns a user object"""

        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        self._session.refresh(user)

        return user

    def find_user_by(self, **kwargs: Dict[str, Any]) -> User:
        """
        This method takes in a key worded value and returns
        the first row found in the users table as
        filtered by the kwargs
        """
        user = self._session.query(User).filter_by(**kwargs).first()
        if not user:
            raise NoResultFound

        return user
