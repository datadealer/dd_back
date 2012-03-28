import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'pyramid',
    'CherryPy',
    ]

setup(name='dd_back',
      version='0.0.1',
      description='dd_back',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='metaflimmer',
      author_email='ai@metaflimmer.at',
      url='http://datadealer.net',
      keywords='web pyramid datadealer',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="dd_back",
      entry_points = """\
      [paste.app_factory]
      main = dd_back:main
      """,
      )

