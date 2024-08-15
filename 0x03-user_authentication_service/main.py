#!/usr/bin/env python3
"""This module tests all the endpoints"""

import requests


BASE_URL = 'http://localhost:5000'
EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


def register_user(email: str, password: str) -> None:
    """This method tests API's register_user functionality """
    response = requests.post(f'{BASE_URL}/users', data={
        'email': email, 'password': password
        }, timeout=5)

    assert response.status_code == 200
    assert response.json() == {"email": email, "message": "user created"}


# def log_in_wrong_password(email: str, password: str) -> None:
#     """This method tests loggin in with wrong password"""

#     response = requests.post(f'{BASE_URL}/sessions', data={
#         'email': email, 'password': password
#         }, timeout=5)

#     assert response.status_code == 401


# def log_in(email: str, password: str) -> str:
#     """This method test the API's login functionality"""

#     response = requests.post(f'{BASE_URL}/sessions', data={
#         'email': email, 'password': password
#         }, timeout=5)

#     assert response.status_code == 200
#     assert response.json() == {"email": email, "message": 'logged in'}
#     return response.cookies.get('session_id')


# def profile_unlogged() -> None:
#     """This method tests the API's /profile route"""
#     response = requests.get(f'{BASE_URL}/profile', timeout=5)
#     assert response.status_code == 403


# def profile_logged(session_id: str) -> None:
#     """This method tests the API's /profile route"""

#     response = requests.get(f'{BASE_URL}/profile', cookies={
#         'session_id': session_id
#         }, timeout=5)

#     assert response.status_code == 200
#     assert "email" in response.json()


# def log_out(session_id: str) -> None:
#     """This function tests the API's logout route"""

#     response = requests.delete(f'{BASE_URL}/sessions', cookies={
#         'session_id': session_id
#         }, timeout=5)

#     assert response.status_code == 200


# def reset_password_token(email: str) -> str:
#     """This function tests the API's reset_password route"""

#     response = requests.post(f'{BASE_URL}/reset_password',  data={
#         'email': email
#         }, timeout=5)

#     assert response.status_code == 200
#     return response.json().get("reset_token")


# def update_password(email: str, reset_token: str, new_password: str) -> None:
#     """This function tests the API's reset_password route"""

#     response = requests.get(f'{BASE_URL}/reset_password', data={
#         'email': email, 'reset_token': reset_token,
#         'new_password': new_password
#         }, timeout=5)

#     assert response.status_code == 200
#     assert response.json() == {"email": email, "message": "Password updated"}


if __name__ == "__main__":
    register_user(EMAIL, PASSWD)
    # log_in_wrong_password(EMAIL, NEW_PASSWD)
    # profile_unlogged()
    # session_id = log_in(EMAIL, PASSWD)
    # profile_logged(session_id)
    # log_out(session_id)
    # reset_token = reset_password_token(EMAIL)
    # update_password(EMAIL, reset_token, NEW_PASSWD)
    # log_in(EMAIL, NEW_PASSWD)
