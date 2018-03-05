from setuptools import setup


with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='analyseether',
    packages=['analyseether'],
    include_package_data=True,
    install_requires=[
        'Flask==0.12.2',
        'Flask-SQLAlchemy==2.3.2',
        'Flask-Bcrypt==0.6.2',
        'Flask-DebugToolbar==0.9.2',
        'Flask-Login==0.2.11',
        'Flask-Mail==0.9.1',
        'Flask-Migrate==1.3.0',
        'Flask-Script==2.0.5',
        'Flask-Testing==0.4.2',
        'Flask-WTF',
        'gunicorn==19.7.1',
        'psycopg2>=2.7,<2.8 --no-binary psycopg2',
        'wtforms',

    ],
)
