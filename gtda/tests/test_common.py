# License: GNU AGPLv3
from itertools import chain
from functools import partial
import re

import pytest
import sklearn
from sklearn.utils.estimator_checks import parametrize_with_checks

from gtda.images.preprocessing import Binarizer, Inverter


# mark checks to skip
SKIP_TESTS = {
  'Binarizer':  [],
  'Inverter':  [],
}

# mark tests as a known failure
# TODO: these should be addressed later.
XFAIL_TESTS = {
  'Binarizer':  ["check_transformer_data_not_an_array",
                 "check_transformer_general",
                 "check_transformer_general(readonly_memmap=True)",
                 "check_fit2d_predict1d",
                 "check_fit1d"],
  'Inverter':  ["check_transformer_data_not_an_array",
                "check_transformer_general",
                "check_transformer_general(readonly_memmap=True)",
                "check_fit2d_predict1d",
                "check_fit1d"],
}

# adapted from sklearn.utils.estimator_check v0.22
def _get_callable_name(obj):
    """Get string representation of a function or a partial function name

    Examples
    --------
    >>> def f(x=2): pass
    >>> _get_callable_name(f)
    'f'
    >>> _get_callable_name(partial(f, x=1))
    'f(x=1)'
    """
    if not isinstance(obj, partial):
        return obj.__name__

    if not obj.keywords:
        return obj.func.__name__

    kwstring = ",".join(["{}={}".format(k, v)
                         for k, v in obj.keywords.items()])
    return "{}({})".format(obj.func.__name__, kwstring)


def _get_estimator_name(estimator):
    """Get string representation for classes and class instances
    
    Examples
    --------
    >>> from sklearn.preprocessing import StandardScaler
    >>> _get_estimator_name(StandardScaler)
    'StandardScaler'
    >>> _get_estimator_name(StandardScaler())
    'StandardScaler'
    """
    if isinstance(estimator, type):
       # this is class
       return estimator.__name__
    else:
       # this an instance
       return estimator.__class__.__name__



@parametrize_with_checks(
    [Binarizer, Inverter]
)
def test_sklearn_api(check, estimator, request):
    estimator_name = _get_estimator_name(estimator)
    check_name = _get_callable_name(check)

    if check_name in SKIP_TESTS[estimator_name]:
        # skip this test
        pytest.skip()

    if check_name in XFAIL_TESTS[estimator_name]:
        # mark tests as a known failure
        request.applymarker(pytest.mark.xfail(run=True, reason='known failure'))
    
    check(estimator)
