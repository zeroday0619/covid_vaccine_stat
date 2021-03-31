from pydantic import ValidationError

from covid_vaccine_stat import sync_request
from covid_vaccine_stat.model import VACCINE_STAT_API

from . import api_key


def check_type(obj):
    # convert ValidationError to TypeError if the obj does not match the expected type
    try:
        VACCINE_STAT_API(**obj)
    except ValidationError as ve:
        raise TypeError(str(ve.errors()))

    return True  # allow constructs like assert check_type(x, List[float])


def test_sync_request():
    res = sync_request.fetch(api_key=api_key)
    assert res == res
    return check_type(obj=res.dict())
