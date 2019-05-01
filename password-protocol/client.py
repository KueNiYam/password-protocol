import requests
import hashlib
import secrets

def sign_in():
    id = input('id: ')
    password = input('password: ')
    salt = secrets.token_hex(32)
    pw_hash = _slow_hash((password + salt).encode('utf-8'))

    data = {'type': 'sign_in', 'id':id, 'pw_hash':pw_hash, 'salt':salt}
    response = requests.post('http://127.0.0.1:5000/members', json=data)
    return response.text

def _slow_hash(value: bytes, count=1000000):
    """
    param
    : value: <bytes> 해시할 값
    : count: <int> 횟수

    return <hex>
    """
    while count > 0 :
        value = hashlib.sha256(value).digest()
        count -= 1

    return value.hex()

def sign_up():
    id = input('id: ')
    password = input('password: ')
    salt = _get_salt(id)
    pw_hash = _slow_hash((password + salt).encode('utf-8'))
    data = {'type': 'sign_up', 'id':id, 'pw_hash':pw_hash}
    response = requests.post('http://127.0.0.1:5000/members', json=data)
    return response.text

def _get_salt(id):
    response = requests.get('http://127.0.0.1:5000/members/' + id + '/salt')
    return response.json()['salt']

if __name__ == '__main__':
    print(sign_in())
    print(sign_up())
