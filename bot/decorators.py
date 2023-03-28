from functools import wraps

def user_required(func):
    @wraps(func)
    def wrapper(self, message, *args, **kwargs):
        if not message.user:
            return self.handle_auth_error(message)
        else:
            return func(self, message, *args, **kwargs)
    return wrapper
