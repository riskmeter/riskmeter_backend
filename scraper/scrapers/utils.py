import asyncio, functools


def await_func(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            loop = asyncio.get_event_loop()
            return loop.run_until_complete(func(*args, **kwargs))
        except RuntimeError as r:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            return loop.run_until_complete(func(*args, **kwargs))

    return wrapper
