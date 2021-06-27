# import pytest

from kasa import Auth
from .conftest import pytestmark

async def test_authenticator(auth):
    assert b'\x04gf\xe9\xc8hO\xb5O\\G\x97\xb0\xbfTZ' == auth.authenticator()

async def test_owner(auth):
    assert b']ZX.Z\xdf\x89n\xd6\xe1GLp\x0bH\x1a' == auth.owner()

async def test_md5user(auth):
    assert b']ZX.Z\xdf\x89n\xd6\xe1GLp\x0bH\x1a' == auth.md5user()

async def test_md5password(auth):
    assert b'\xa0)\xd0\xdf\x84\xebUI\xc6A\xe0J\x9e\xf3\x89\xe5' == auth.md5password()

async def test_md5auth(auth):
    assert b'\x04gf\xe9\xc8hO\xb5O\\G\x97\xb0\xbfTZ' == auth.md5auth()
