from setuptools import setup, find_packages


GENERATOR = ['faker', 'bcrypt','faker-commerce', 'psycopg2-binary', 'pandas']

TEST = [
    'pytest==7.3.1',
    'mock==5.0.2',
    'types-mock==5.0.0.6',
    'pytest-cov==4.1.0',
]

setup(
    name='de-streaming-demo',
    maintainer='Gergo Nagy',
    install_requires=[],
    extras_require={

        'test': TEST,
        'generator': GENERATOR,
    },
)
