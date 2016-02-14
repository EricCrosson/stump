from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='stump',
      version='0.1',
      description='Logs program flow with decorators',
      long_description=readme(),
      url='http://github.com/EricCrosson/stump',
      setup_requires=['pytest-runner',],
      tests_require=['pytest'],
      author='Eric Crosson',
      author_email='eric.s.crosson@utexas.edu',
      license='GPLv3',
      packages=['stump'],
      include_package_data=True,
      zip_safe=False)
