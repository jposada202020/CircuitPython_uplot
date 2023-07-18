.. image:: https://readthedocs.org/projects/circuitpython-uplot/badge/?version=latest
    :target: https://circuitpython-uplot.readthedocs.io/
    :alt: Documentation Status

.. image:: https://github.com/jposada202020/CircuitPython_uplot/workflows/Build%20CI/badge.svg
    :target: https://github.com/jposada202020/CircuitPython_uplot/actions
    :alt: Build Status

.. image:: https://img.shields.io/pypi/v/circuitpython-uplot.svg
    :alt: latest version on PyPI
    :target: https://pypi.python.org/pypi/circuitpython-uplot

.. image:: https://static.pepy.tech/personalized-badge/circuitpython-uplot?period=total&units=international_system&left_color=grey&right_color=blue&left_text=Pypi%20Downloads
    :alt: Total PyPI downloads
    :target: https://pepy.tech/project/circuitpython-uplot

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: Code Style: Black

Framework to display different graphical plots in displayio.
Take a look in the `examples <https://circuitpython-uplot.readthedocs.io/en/latest/examples.html>`_ section in RTD to see the gallery

For detailed view of the library please refer to the `Quick start guide <https://circuitpython-uplot.readthedocs.io/>`_

.. image:: https://github.com/jposada202020/CircuitPython_uplot/blob/main/docs/readme.png

.. image:: https://github.com/jposada202020/CircuitPython_uplot/blob/main/docs/readme2.png


Below a picture oa a real live application. for more information visit the project `page <https://github.com/casainho/temperature_humidity_sensor_eink_display>`_. Thanks to @Casainho

.. image:: https://github.com/jposada202020/CircuitPython_uplot/blob/main/docs/logging.png


Dependencies
=============
This library depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_

This library is resource consuming, may or may not with some CircuitPython supported devices.
Tinker it as you wish in order to work.

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://circuitpython.org/libraries>`_
or individual libraries can be installed using
`circup <https://github.com/adafruit/circup>`_.


Installing from PyPI
=====================

On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/circuitpython-uplot/>`_.
To install for current user:

.. code-block:: shell

    pip3 install circuitpython-uplot

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install circuitpython-uplot

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .venv
    source .env/bin/activate
    pip3 install circuitpython-uplot

Installing to a Connected CircuitPython Device with Circup
==========================================================

Make sure that you have ``circup`` installed in your Python environment.
Install it with the following command if necessary:

.. code-block:: shell

    pip3 install circup

With ``circup`` installed and your CircuitPython device connected use the
following command to install:

.. code-block:: shell

    circup install circuitpython_uplot

Or the following command to update an existing version:

.. code-block:: shell

    circup update

Usage Example
=============

To learn how to use the library please refer to the examples folder or the
`Quick start guide <https://circuitpython-uplot.readthedocs.io/>`_

Documentation
=============
API documentation for this library can be found on `Read the Docs <https://circuitpython-uplot.readthedocs.io/>`_.


Contributing
============

Contributions are welcome!
