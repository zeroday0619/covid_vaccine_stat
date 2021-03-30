from typing import List, Optional

from pydantic import BaseModel, validator


class VACCINE_STAT_MODEL(BaseModel):
    """VACCINE_STAT_MODEL

    >>> baseDate: str                # 통계 기준일자
    >>> sido: str                    # 지역명칭
    >>> firstCnt: int                 # 당일 통계(1차 접종)
    >>> secondCnt: int               # 당일 통계(2차 접종)
    >>> totalFirstCnt: int           # 전체 누적 통계(1차 접종)
    >>> totalSecondCnt: int          # 전체 누적 통계(2차 접종)
    >>> accumulatedFirstCnt: int     # 전일까지의 누적 통계 (1차 접종)
    >>> accumulatedSecondCnt: int    # 전일까지의 누적 통계 (2차 접종)
    """

    baseDate: str
    sido: str
    firstCnt: int
    secondCnt: int
    totalFirstCnt: int
    totalSecondCnt: int
    accumulatedFirstCnt: int
    accumulatedSecondCnt: int


class VACCINE_STAT_API(BaseModel):
    """
    {
        "page": 0,
        "perPage": 0,
        "totalCount": 0,
        "currentCount": 0,
        "data": [{
            "baseDate": "string",
            "sido": "string",
            "firstCnt": 0,
            "secondCnt": 0,
            "totalFirstCnt": 0,
            "totalSecondCnt": 0,
            "accumulatedFirstCnt": 0,
            "accumulatedSecondCnt": 0
        }]
    }
    """

    page: int
    perPage: int
    totalCount: int
    currentCount: int
    data: List[VACCINE_STAT_MODEL]


class ParameterValidateModel(BaseModel):
    """Parameters Validator

    >>> page: int = 1
    >>> perPage: int = 10
    >>> returnType: str = "json"
    >>> baseDateEQ: Optional[str] = None
    >>> baseDateLT: Optional[str] = None
    >>> baseDateLTE: Optional[str] = None
    >>> baseDateGT: Optional[str] = None
    >>> baseDateGTE: Optional[str] = None
    >>> sidoEQ: Optional[str] = None
    """

    page: int = 1
    perPage: int = 10
    returnType: str = "json"
    baseDateEQ: Optional[str] = None
    baseDateLT: Optional[str] = None
    baseDateLTE: Optional[str] = None
    baseDateGT: Optional[str] = None
    baseDateGTE: Optional[str] = None
    sidoEQ: Optional[str] = None

    @validator("returnType")
    def return_type_match(cls, value: str) -> str:
        _value = value.lower()
        if _value == "json":
            return _value
        elif _value == "xml":
            return _value
        else:
            if _value is None:
                raise TypeError("None is not support return type.")
            else:
                raise TypeError(f"{_value} is not support return type.")
