from enum import Enum


# Represents http method type
class HttpMethod(Enum):
    GET = 1,
    POST = 2,
    PUT = 3,
    PATCH = 4,
    DELETE = 5