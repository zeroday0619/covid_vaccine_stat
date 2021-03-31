__author__ = "Euiseo Cha"
__copyright__ = "Copyright (C) 2021 Euiseo Cha <zeroday0619@kakao.com>"
__license__ = "MIT License"
__version__ = "0.0.2"

from covid_vaccine_stat.async_request import AsyncRequest as _AsyncRequest
from covid_vaccine_stat.sync_request import SyncRequest as _SyncRequest

sync_request = _SyncRequest
async_request = _AsyncRequest

__all__ = ["sync_request", "async_request"]
