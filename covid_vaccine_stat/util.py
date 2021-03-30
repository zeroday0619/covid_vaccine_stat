from typing import AnyStr, Dict

from covid_vaccine_stat.model import ParameterValidateModel


def add_authorize_parameter(source: Dict[str, AnyStr], api_key: str) -> Dict[str, AnyStr]:
    source.update(dict(serviceKey=api_key))
    return source


# Error: Function is missing a type annotation for one or more arguments [no-untyped-def]
def build_parameter(*args, **kwargs) -> Dict[str, AnyStr]:
    """build parameter

    :return: parameter
    """
    raw_parameter = ParameterValidateModel(**dict(*args, **kwargs))
    parameter = raw_parameter.dict()
    filtered = {k: v for k, v in parameter.items() if v is not None}
    parameter.clear()
    parameter.update(filtered)
    return parameter
