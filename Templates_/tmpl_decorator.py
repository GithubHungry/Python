from functools import wraps


def decorator_name(func: object):
    @wraps(func)
    def wrapper(*arg, **kwargs):
        # 1. Code to execute BEFORE calling the decorated function

        # 2. Вызов декорируемой функции и возврат полученных от нее результатов
            return func(*arg,**kwargs)

        # 3. Код для выполнения ВМЕСТО вызова декорируемой функции

    return wrapper
