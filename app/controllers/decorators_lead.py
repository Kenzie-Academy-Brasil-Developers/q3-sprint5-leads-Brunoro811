from re import match,fullmatch
from functools import wraps
from http import HTTPStatus

from flask import request

def verify_keys(correct_keys: list[str]):
    def received_function(function):
        @wraps(function)
        def wrapper():
            request_json: dict = request.get_json()
            lista_keys_received = list(request_json.keys())
            lista_keys_received.sort()
            correct_keys.sort()
            print(request_json)
            try:
                count = 0
                if len(correct_keys) > len(lista_keys_received):
                    return {"error": "some keys is missing!"}, 400
                if len(correct_keys) < len(lista_keys_received):
                    return {"error": "some keys is left over!"}, 400
                for key in lista_keys_received:
                    if not key == correct_keys[count]:
                        raise KeyError
                    count += 1
                return function()
            except KeyError:
                return {
                    "error": "key(s) incorrect",
                    "expected": correct_keys,
                    "received": list(request_json.keys())
                }, 400
        return wrapper
    return received_function


def validate_values(func):
    @wraps(func)
    def wrapper():
        try:
            data = request.get_json()

            if(data.get('phone')):
                phone = data['phone']
                regex_phone = "^\([1-9]{2}\)(?:[2-8]|9[0-9])[0-9]{3}\-[0-9]{4}$"
                if not match(regex_phone,phone):
                    return {
                        "error": "number's format incorrect or invalid!",
                        "should be": "(xx)xxxxx-xxxx "
                        },HTTPStatus.UNPROCESSABLE_ENTITY
            if(data.get('email')):
                email = data['email']
                regex_email = "^[\w\.]+@([\w-]+\.)+[\w-]{2,4}$"
                if not match(regex_email,email):
                    return {
                        "error": "email in format incorrect",
                        "should be": " exemplo@gmail.com,exemplo@gmail.com.br "
                        },HTTPStatus.UNPROCESSABLE_ENTITY
            
            return func()
        except Exception as e:
            raise e
    return wrapper

def verify_all_types_string(func):
    @wraps(func)
    def wrapper():
        try:
            values = list(request.get_json().values())
            values_error = []
            for element in values:
                if type(element) != str:
                    values_error.append(element)
            if(values_error):
                raise TypeError                
            return func()
        except AttributeError:
            return {'error': "should be an email"}, HTTPStatus.NOT_FOUND
        except TypeError:
            return{
                'error': 'all values must be str',
                'wrong_received': values_error
            },HTTPStatus.UNPROCESSABLE_ENTITY

        except Exception as e:
            raise e
    return wrapper