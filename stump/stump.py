#!/usr/bin/env python
# Written by Eric Crosson
# 2016-02-13 <3

import inspect
import logging


def parametrized(dec):
    def layer(*args, **kwargs):
        def repl(f):
            return dec(f, *args, **kwargs)
        return repl
    return layer


def configure(logger):
    """Pass stump a logger to use."""
    global LOGGER
    LOGGER = logger


@parametrized
def ret(f, *args, **kwargs):
    """Automatically log progress on function entry and exit. Default logging
    value: info. The function's return value will be included in the logs.

    *Logging with values contained in the parameters of the decorated function*
    Message (args[0]) may be a string to be formatted with parameters passed to
    the decorated function. Each '{varname}' will be replaced by the value of
    the parameter of the same name.

    *Keyword parameters*
    - log :: integer
      - Specifies a custom level of logging to pass to the active logger.
      - Default: INFO

    *Exceptions:*
    - IndexError and ValueError
      - will be returned if *args contains a string that does not correspond to
        a parameter name of the decorated function, or if there are more '{}'s
        than there are *args.

    """
    kwargs.update({'print_return': True})
    return _stump(f, *args, **kwargs)


@parametrized
def pre(f, *args, **kwargs):
    """Automatically log progress on function entry. Default logging value: 
    info.

    *Logging with values contained in the parameters of the decorated function*
    Message (args[0]) may be a string to be formatted with parameters passed to
    the decorated function. Each '{varname}' will be replaced by the value of
    the parameter of the same name.

    *Keyword parameters*
    - log :: integer
      - Specifies a custom level of logging to pass to the active logger.
      - Default: INFO

    *Exceptions:*
    - IndexError and ValueError
      - will be returned if *args contains a string that does not correspond to
        a parameter name of the decorated function, or if there are more '{}'s
        than there are *args.

    """
    kwargs.update({'prefix_only': True})
    return _stump(f, *args, **kwargs)


@parametrized
def post(f, *args, **kwargs):
    """Automatically log progress on function exit. Default logging value: 
    info.

    *Logging with values contained in the parameters of the decorated function*
    Message (args[0]) may be a string to be formatted with parameters passed to
    the decorated function. Each '{varname}' will be replaced by the value of
    the parameter of the same name.

    *Keyword parameters*
    - log :: integer
      - Specifies a custom level of logging to pass to the active logger.
      - Default: INFO

    *Exceptions:*
    - IndexError and ValueError
      - will be returned if *args contains a string that does not correspond to
        a parameter name of the decorated function, or if there are more '{}'s
        than there are *args.

    """
    kwargs.update({'postfix_only': True})
    return _stump(f, *args, **kwargs)


@parametrized
def put(f, *args, **kwargs):
    """Automatically log progress on function entry and exit. Default logging
    value: info.

    *Logging with values contained in the parameters of the decorated function*
    Message (args[0]) may be a string to be formatted with parameters passed to
    the decorated function. Each '{varname}' will be replaced by the value of
    the parameter of the same name.

    *Keyword parameters*
    - log :: integer
      - Specifies a custom level of logging to pass to the active logger.
      - Default: INFO

    *Exceptions:*
    - IndexError and ValueError
      - will be returned if *args contains a string that does not correspond to
        a parameter name of the decorated function, or if there are more '{}'s
        than there are *args.

    """
    return _stump(f, *args, **kwargs)


def _stump(f, *args, **kwargs):
    """Worker for the common actions of all stump methods, aka the secret
    sauce.

    *Keyword parameters*
    - log :: integer
      - Specifies a custom level of logging to pass to the active logger.
      - Default: INFO
    - print_return :: bool
      - include the return value in the functions exit message
    - postfix_only :: bool
      - omit the functions entering message
    - prefix_only :: bool
      - omit the functions exiting message

    *Exceptions:*
    - IndexError and ValueError
      - will be returned if *args contains a string that does not correspond to
        a parameter name of the decorated function, or if there are more '{}'s
        than there are *args.

    """
    global LOGGER
    def aux(*xs, **kws):
        f_kws = kws.copy()
        f_kws.update(dict(zip(inspect.getfullargspec(f).args, xs)))
        # FIXME: pass message in directly, *args will always be length 1
        try:
            message = list(args).pop(0)
        except:
            message = f.__name__
        try:
            report = '{}:{}'.format(f.__name__, message.format(**f_kws))
        except KeyError:
            report = '{}:KeyError in decorator usage'.format(f.__name__)

        level = kwargs.get('log', logging.INFO)
        post = kwargs.get('postfix_only', False)
        pre = kwargs.get('prefix_only', False)
        print_return = kwargs.get('print_return', False)

        if not post: LOGGER.log(level, '%s...', report)
        try:
            ret = f(*xs, **kws)
        except Exception as e:
            LOGGER.log(level, '%s...threw exception %s with message %s',
                       report, type(e).__name__, str(e))
            raise
        if not pre:
            if print_return:
                LOGGER.log(level, '%s...done (returning %s)', report, ret)
            else:
                LOGGER.log(level, '%s...done', report)
        return ret
    return aux
