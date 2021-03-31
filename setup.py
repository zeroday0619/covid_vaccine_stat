import re
from setuptools import setup

requirements = []
with open('requirements.txt') as f:
    # noinspection PyRedeclaration
    requirements = f.read().splitlines()

version = ''
with open('covid_vaccine_stat/__init__.py') as f:
    # noinspection PyRedeclaration
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('version is not set')

readme = ''
with open('README.md') as f:
    readme = f.read()

setup(
    name='covid_vaccine_stat', author='zeroday0619',
    url='https://github.com/zeroday0619/covid_vaccine_stat',
    project_urls={"Issue tracker": "https://github.com/zeroday0619/covid_vaccine_stat/issues"},
    version=version,
    packages=["covid_vaccine_stat"],
    license='MIT',
    long_description=readme,
    long_description_content_type="text/markdown",
    description="""
    공공데이터 포털 ( [data.go.kr](https://www.data.go.kr/) ) 에서 제공하는 코로나19 예방접종 실적 통계 데이터 조회 서비스 API Wrapper
    """,
    include_package_data=True,
    install_requires=requirements,
    python_requires='>=3.7.0',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Natural Language :: Korean',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
