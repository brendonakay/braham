#!/usr/bin/env python
#
# http://flask.pocoo.org/docs/1.0/tutorial/tests/
#
from braham_flask import create_app


def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing


def test_hello(client):
    response = client.get('/hello')
    assert response.data == b'Hello, World!'
