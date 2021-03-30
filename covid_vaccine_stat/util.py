# mypy: disallow-untyped-defs
from typing import Dict, Optional, Union

from covid_vaccine_stat.model import ParameterValidateModel


def add_authorize_parameter(source: Dict[str, str], api_key: str) -> Dict[str, str]:
    temp: Dict[str, str] = dict(serviceKey=api_key)
    source.update(temp)
    return source


# Error: Function is missing a type annotation  [no-untyped-def]
def build_parameter(
    *args: Optional[Union[str, int]], **kwargs: Optional[Union[str, int]]
) -> Dict[str, str]:
    """build parameter

    :return: parameter
    """
    raw_parameter = ParameterValidateModel(**dict(*args, **kwargs))
    parameter = raw_parameter.dict()
    filtered = {k: v for k, v in parameter.items() if v is not None}
    parameter.clear()
    parameter.update(filtered)
    return parameter
