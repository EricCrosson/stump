Stump
.. image:: https://travis-ci.org/EricCrosson/stump.svg?branch=master
   :target: https://travis-ci.org/EricCrosson/stump
=====

-  `What is stump?`_
-  `Installation`_
-  `Usage`_
-  `License`_

What is stump?
--------------

**Stump:**

*n.* the lower end of a tree or plant left after the main part is
removed

**Log**

*n.* a portion or length of the trunk or of a large limb of a felled
tree

Stump is a **logging utility for Python** that uses the `logging
module`_ under the covers. However, a stump is a different part of a
tree than a log and as such should be utilized differently. Stump offers
various `method decorators`_ that really cover all the bases of logging
for debugging. Stump’s method decorators are flexible and concise, act
as additional documentation, don’t clutter the main code of the method
body and accept a natural format string that is easy to form and read.

Installation
------------

The publication of this process is still in the works. Check back
shortly.

Usage
-----

Insert the stump library and configure the stump logger

.. code-block:: python

      #!/usr/bin/env python
      import stump

      # configure a logger for stump
      import sys
      import logging
      logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
      logger = logging.getLogger()

      stump.configure(logger)

And decorate some methods. Stump allows you to interpolate a string
representation of the parameter values to decorated methods by simply
wrapping the parameter name in curly braces.

.. code-block:: python

      import random
      @stump.ret('"Calculating" boost for car {car}')
      def car_boost(car):
          return random.random() * 100

      @stump.pre()
      def ready(): pass
      @stump.pre()
      def set(): pass
      @stump.post()
      def go(): pass

      @stump.ret('Racing {car}')
      def race(car):
          luck = car_boost(car)
          return random.randint(1, round(luck))

      ready()
      set()
      go()
      race('wacky')

This example logs the following events

.. code:: text

      INFO:root:ready:ready...
      INFO:root:set:set...
      INFO:root:go:go...done
      INFO:root:race:Racing wacky...
      INFO:root:car_boost:"Calculating" boost for car wacky...
      INFO:root:car_boost:"Calculating" boost for car wacky...done (returning 11.857944115557483)
      INFO:root:race:Racing wacky...done (returning 2)

License
-------

This code is released under the MIT license.

.. _What is stump?: #what-is-stump
.. _Installation: #installation
.. _Usage: #usage
.. _License: #license
.. _logging module: https://docs.python.org/3/library/logging.html
.. _method decorators: https://www.python.org/dev/peps/pep-0318/
