Stump
=====

.. image:: https://travis-ci.org/EricCrosson/stump.svg?branch=master
   :target: https://travis-ci.org/EricCrosson/stump
   :alt: Travis-CI Build Status

-  `What is stump?`_

-  `Installation`_

-  `Usage`_

   -  `Examples`_

-  `License`_

.. role:: python(code)
   :language: python

What is stump?
--------------

**Stump:**

*n.* the lower end of a tree or plant left after the main part is
removed

**Log:**

*n.* a portion or length of the trunk or of a large limb of a felled
tree

:python:`stump` is a **logging utility for Python** that uses the `standard
logging module`_ under the covers. However, a stump is a different part of a
tree than a log and as such should be utilized differently. :Python:`stump`
offers various `method decorators`_ that really cover all the bases of logging
for debugging. :Python:`stump`’s method decorators are flexible and concise, act
as additional documentation, don’t clutter the main code of the method body and
accept a natural format string that is easy to form and read.

Installation
------------

Install from `pip`_

.. code-block:: bash

   pip install stump

Alternatively, clone this repo and install from your local copy

.. code-block:: bash

   git clone https://github.com/EricCrosson/stump
   cd stump
   python setup.py install


Usage
-----

Once installed simply :python:`import stump` and pass a logger to
:python:`stump.configure`, as demonstrated in the `Examples`_ section.

The different :python:`stump` decorators all inherit the same functionality,
with minor behavioral differences. Each decorator accepts a logging string as
the first argument. This string may contain the values of the decorated method's
parameters. For example, to log the values of parameters passed to
:python:`accelerate` the following format string could be used

.. code-block:: python

       @stump.put('Object is {weight} lbs with {gravity} m/s^2 acceleration')
       def accelerate(weight, gravity):
           work()


If invoked by :python:`accelerate(42, 9.8)` the logs generated would be

.. code-block:: text

       INFO:root:accelerate:Object is 42 lbs with 9.8 m/s^2 acceleration...
       INFO:root:accelerate:Object is 42 lbs with 9.8 m/s^2 acceleration...done

The standard decorator, :python:`stump.put`, prints a message upon entering and
exiting a method. The below table describes the public api exposed by :python:`stump`.

:python:`stump.put`
        Print a message upon entering and exiting the method

:python:`stump.pre`
        Print a message only upon entering the method

:python:`stump.post`
        Print a message only upon exiting the method

:python:`stump.date`
        Like :python:`stump.put`, but include a date- and time- stamp

:python:`stump.ret`
        Like :python:`stump.put`, but include the method's return value


Examples
~~~~~~~~

Import the :python:`stump` library and configure the :python:`stump` logger

.. code-block:: python

      #!/usr/bin/env python
      import stump

      # configure a logger for stump
      import sys
      import logging
      logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
      logger = logging.getLogger()

      stump.configure(logger)

And decorate some methods. :Python:`stump` allows you to interpolate a string
representation of the parameter values to decorated methods by simply
wrapping the parameter name in curly braces.

.. code-block:: python

      import random
      @stump.ret('"Calculating" boost for car {car}')
      def car_boost(car):
          return random.random() * 100

      class NoNitrousException(Exception): pass
      @stump.post('Using nitrous')
      def use_nitrous():
          raise NoNitrousException('You never installed nitrous!')

      @stump.pre()
      def ready(): pass
      @stump.pre()
      def set(): pass
      @stump.post()
      def go(): pass

      @stump.ret('Racing {car}')
      def race(car):
          luck = car_boost(car)
          try:
              use_nitrous()
          except:
              pass
          return random.randint(1, round(luck))

      ready()
      set()
      go()
      race('wacky')

This example logs the following events

.. code:: text

      INFO:root:ready...
      INFO:root:set...
      INFO:root:go...done
      INFO:root:race:Racing wacky...
      INFO:root:car_boost:"Calculating" boost for car wacky...
      INFO:root:car_boost:"Calculating" boost for car wacky...done (returning 81.53077859037138)
      INFO:root:use_nitrous:Using nitrous...threw exception NoNitrousException with message You never installed nitrous!
      INFO:root:race:Racing wacky...done (returning 2)

License
-------

This code is released under the MIT license.

.. _What is stump?: #what-is-stump
.. _Installation: #installation
.. _Usage: #usage
.. _License: #license
.. _Examples: #examples
.. _logging module: https://docs.python.org/3/library/logging.html
.. _method decorators: https://www.python.org/dev/peps/pep-0318/
.. _pip: https://pypi.python.org/pypi/pip
