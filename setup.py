from distutils.core import setup

setup(
    name='appodeal-api',
    version='0.1.0',
    author='Aslan',
    author_email='bloogrox@gmail.com',
    packages=['appodeal-api'],
    url='git@github.com:Pavel-Guseynov/appodeal-api.git',
    description='Python client for Appodeal API',
    install_requires=[
        "requests",
    ],
    dependency_links=[
        "git+https://github.com/bloogrox/http_build_query.git#egg=http_build_query"
    ],
)
