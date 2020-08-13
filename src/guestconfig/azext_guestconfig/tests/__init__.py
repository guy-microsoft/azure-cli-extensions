# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
import inspect
import os
import sys
import traceback
from azure.core.exceptions import AzureError
from azure.cli.testsdk.exceptions import CliTestError, CliExecutionError, JMESPathCheckAssertionError


__path__ = __import__('pkgutil').extend_path(__path__, __name__)
exceptions = []


def try_manual(func):
    def import_manual_function(origin_func):
        from importlib import import_module
        decorated_path = inspect.getfile(origin_func)
        module_path = __path__[0]
        if not decorated_path.startswith(module_path):
            raise Exception("Decorator can only be used in submodules!")
        manual_path = os.path.join(
            decorated_path[module_path.rfind(os.path.sep) + 1:])
        manual_file_path, manual_file_name = os.path.split(manual_path)
        module_name, _ = os.path.splitext(manual_file_name)
        manual_module = "..manual." + \
            ".".join(manual_file_path.split(os.path.sep) + [module_name, ])
        return getattr(import_module(manual_module, package=__name__), origin_func.__name__)

    def get_func_to_call():
        func_to_call = func
        try:
            func_to_call = import_manual_function(func)
            print("Found manual override for {}(...)".format(func.__name__))
        except (ImportError, AttributeError):
            pass
        return func_to_call

    def wrapper(*args, **kwargs):
        func_to_call = get_func_to_call()
        print("running {}()...".format(func.__name__))
        try:
            return func_to_call(*args, **kwargs)
        except (AssertionError, AzureError, CliTestError, CliExecutionError, JMESPathCheckAssertionError) as e:
            print("--------------------------------------")
            print("step exception: ", e)
            print("--------------------------------------", file=sys.stderr)
            print("step exception in {}: {}".format(func.__name__, e), file=sys.stderr)
            traceback.print_exc()
            exceptions.append((func.__name__, sys.exc_info()))

    if inspect.isclass(func):
        return get_func_to_call()
    return wrapper


def raise_if():
    if exceptions:
        if len(exceptions) <= 1:
            raise exceptions[0][1][1]
        message = "{}\nFollowed with exceptions in other steps:\n".format(str(exceptions[0][1][1]))
        message += "\n".join(["{}: {}".format(h[0], h[1][1]) for h in exceptions[1:]])
        raise exceptions[0][1][0](message).with_traceback(exceptions[0][1][2])
