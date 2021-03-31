[코로나 백신 예방 접종 통계 API](https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15077756#/API%20%EB%AA%A9%EB%A1%9D/GETvaccine-stat) Wrapper
=================================================================================
[![Upload Python Package](https://github.com/zeroday0619/covid_vaccine_stat/actions/workflows/python-publish.yml/badge.svg)](https://github.com/zeroday0619/covid_vaccine_stat/actions/workflows/python-publish.yml)
[![test](https://github.com/zeroday0619/covid_vaccine_stat/actions/workflows/test.yml/badge.svg)](https://github.com/zeroday0619/covid_vaccine_stat/actions/workflows/test.yml)
[![codecov](https://codecov.io/gh/zeroday0619/covid_vaccine_stat/branch/main/graph/badge.svg)](https://codecov.io/gh/zeroday0619/covid_vaccine_stat)
[![CodeFactor](https://www.codefactor.io/repository/github/zeroday0619/covid_vaccine_stat/badge)](https://www.codefactor.io/repository/github/zeroday0619/covid_vaccine_stat)
[![lint](https://github.com/zeroday0619/covid_vaccine_stat/actions/workflows/lint.yml/badge.svg)](https://github.com/zeroday0619/covid_vaccine_stat/actions/workflows/lint.yml)

#### 공공데이터 포털 ( [data.go.kr](https://www.data.go.kr/) ) 에서 제공하는 코로나19 예방접종 실적 통계 데이터 조회 서비스 API Wrapper


## **Usage**

### Install module
```shell
pip install covid-vaccine-stat
```
or
```shell
pip install git+https://github.com/zeroday0619/covid_vaccine_stat.git
```

### Example
1. #### Synchronous
```python
import json
from covid_vaccine_stat import sync_request

api_key = "# data.go.kr 에서 발급 받은 API Key #"

res = sync_request.fetch(api_key=api_key)
json_data = json.dumps(
    res.data[0].json(), 
    ensure_ascii=False, 
    escape_forward_slashes=False
)
print(json_data)
```
2. #### Asynchronous
```python
import json
import asyncio
from covid_vaccine_stat import async_request

api_key = "# data.go.kr 에서 발급 받은 API Key #"

loop = asyncio.get_event_loop()
res = loop.run_until_complete(async_request.fetch(api_key=api_key))
json_data = json.dumps(
    res.data[0].json(),
    ensure_ascii=False,
    escape_forward_slashes=False
)
print(json_data)
```

## License
Copyright (c) 2021 Euiseo Cha <zeroday0619@kakao.com>

Distributed under the [**MIT License**](LICENSE)
