from setuptools import setup, find_packages


setup(
    name='first-fastAPI',
    version='0.0.1',
    author='ArtemVerzun',
    description='API приложение',
    packages=find_packages(),
    install_requires=[
        'fastapi==0.70.0',
        'uvicorn==0.15.0',
        'starlette==0.16.0',
        'SQLAlchemy==1.4.26',
        'pytest==6.2.5',
        'pydantic==1.10.12',
        'requests==2.26.0',
    ],
    scripts=['main.py']
)
