import pytest
from pydantic import ValidationError

from covid_vaccine_stat import async_request
from covid_vaccine_stat.model import VACCINE_STAT_API

from . import api_key


def check_type(obj: dict):
    # convert ValidationError to TypeError if the obj does not match the expected type
    try:
        VACCINE_STAT_API(**obj)
    except ValidationError as ve:
        raise ve

    return True  # allow constructs like assert check_type(x, List[float])


@pytest.mark.asyncio
async def test_async_request():
    res = await async_request.fetch(api_key=api_key)
    assert id(res) == id(res) and res == res
    return check_type(obj=res.dict())
