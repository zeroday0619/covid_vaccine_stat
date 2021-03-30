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

setup(name='covid_vaccine_stat',
      author='Euiseo Cha',
      url='https://github.com/zeroday0619/covid_vaccine_stat',
      project_urls={
          "Issue tracker": "https://github.com/zeroday0619/covid_vaccine_stat/issues",
      },
      version=version,
      packages=["covid_vaccine_stat"],
      license='MIT',
      description="""A Python wrapper for the [https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk
      =15077756](https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15077756)""",
      include_package_data=True,
      install_requires=requirements,
      python_requires='>=3.7.0',
      classifiers=[
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
      ]
      )
