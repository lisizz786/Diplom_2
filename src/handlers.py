class BaseURLs:
    STELLAR_BURGERS = 'https://stellarburgers.nomoreparties.site'


class UserAPIPaths:
    REGISTER_USER = '/api/auth/register'
    USER_LOGIN = '/api/auth/login'
    UPDATE_USER_PROFILE = '/api/auth/user'
    REMOVE_USER = '/api/auth/user'


class OrderAPIPaths:
    PLACE_ORDER = '/api/orders'
    VIEW_USER_ORDERS = '/api/orders'


class HTTPHeaders:
    JSON_HEADER = {"Content-Type": "application/json"}
