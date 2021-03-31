from typing import Optional

import aiohttp

from covid_vaccine_stat._conf import API_URL
from covid_vaccine_stat.error import RequestError
from covid_vaccine_stat.model import VACCINE_STAT_API
from covid_vaccine_stat.util import add_authorize_parameter, build_parameter


class AsyncRequest(object):
    @classmethod
    async def fetch(
        cls,
        api_key: str,
        page: int = 1,
        per_page: int = 10,
        return_type: str = "json",
        base_date_eq: Optional[str] = None,
        base_date_lt: Optional[str] = None,
        base_date_lte: Optional[str] = None,
        base_date_gt: Optional[str] = None,
        base_date_gte: Optional[str] = None,
        sido_eq: Optional[str] = None,
    ) -> VACCINE_STAT_API:
        """fetch API

        :param api_key: api key
        :param page: not documentation
        :param per_page: not documentation
        :param return_type: json or xml
        :param base_date_eq: not documentation
        :param base_date_lt: not documentation
        :param base_date_lte: not documentation
        :param base_date_gt: not documentation
        :param base_date_gte: not documentation
        :param sido_eq: not documentation
        :return: response data
        """
        param = add_authorize_parameter(
            source=build_parameter(
                page=page,
                perPage=per_page,
                returnType=return_type,
                baseDateEQ=base_date_eq,
                baseDateLT=base_date_lt,
                baseDateLTE=base_date_lte,
                baseDateGT=base_date_gt,
                baseDateGTE=base_date_gte,
                sidoEQ=sido_eq,
            ),
            api_key=api_key,
        )
        async with aiohttp.ClientSession() as session:
            async with session.get(url=API_URL, params=param) as resp:
                if not resp.status == 200:
                    err = await resp.json()
                    err_msg = err["msg"]
                    raise RequestError(err_msg)
                rs = await resp.json()
        return VACCINE_STAT_API(**rs)
