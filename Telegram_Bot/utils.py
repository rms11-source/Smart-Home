import functools
import sentry_sdk

def logger_factory(logger):
    def debug_requests(f):

        @functools.wraps(f)
        def inner(*args, **kwargs):

            try:
                logger.debug("Called function '{}'".format(f.__name__))
                return f(*args, **kwargs)
            except Exception as e:
                logger.exception("Error in function '{}'".format(f.__name__))
                sentry_sdk.capture_exception(error=e)
                raise

        return inner

    return debug_requests