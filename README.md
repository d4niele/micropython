[![CI badge](https://github.com/micropython/micropython/workflows/unix%20port/badge.svg)](https://github.com/micropython/micropython/actions?query=branch%3Amaster+event%3Apush) [![Coverage badge](https://coveralls.io/repos/micropython/micropython/badge.png?branch=master)](https://coveralls.io/r/micropython/micropython?branch=master)

The MicroPython project
=======================


This is the MicroPython project, which aims to put an implementation
of Python 3.x on microcontrollers and small embedded systems.
You can find the official website at [micropython.org](http://www.micropython.org).

WARNING: this project is in beta stage and is subject to changes of the
code-base, including project-wide name changes and API changes.

MicroPython implements the entire Python 3.4 syntax (including exceptions,
`with`, `yield from`, etc., and additionally `async`/`await` keywords from
Python 3.5). The following core datatypes are provided: `str` (including
basic Unicode support), `bytes`, `bytearray`, `tuple`, `list`, `dict`, `set`,
`frozenset`, `array.array`, `collections.namedtuple`, classes and instances.
Builtin modules include `sys`, `time`, and `struct`, etc. Select ports have
support for `_thread` module (multithreading). Note that only a subset of
Python 3 functionality is implemented for the data types and modules.

MicroPython can execute scripts in textual source form or from precompiled
bytecode, in both cases either from an on-device filesystem or "frozen" into
the MicroPython executable.

See the repository http://github.com/micropython/pyboard for the MicroPython
board (PyBoard), the officially supported reference electronic circuit board.

Major components in this repository:
- py/ -- the core Python implementation, including compiler, runtime, and
  core library.
- mpy-cross/ -- the MicroPython cross-compiler which is used to turn scripts
  into precompiled bytecode.
- ports/unix/ -- a version of MicroPython that runs on Unix.
- ports/stm32/ -- a version of MicroPython that runs on the PyBoard and similar
  STM32 boards (using ST's Cube HAL drivers).
- ports/minimal/ -- a minimal MicroPython port. Start with this if you want
  to port MicroPython to another microcontroller.
- tests/ -- test framework and test scripts.
- docs/ -- user documentation in Sphinx reStructuredText format. Rendered
  HTML documentation is available at http://docs.micropython.org.

Additional components:
- ports/bare-arm/ -- a bare minimum version of MicroPython for ARM MCUs. Used
  mostly to control code size.
- ports/teensy/ -- a version of MicroPython that runs on the Teensy 3.1
  (preliminary but functional).
- ports/pic16bit/ -- a version of MicroPython for 16-bit PIC microcontrollers.
- ports/cc3200/ -- a version of MicroPython that runs on the CC3200 from TI.
- ports/esp8266/ -- a version of MicroPython that runs on Espressif's ESP8266 SoC.
- ports/esp32/ -- a version of MicroPython that runs on Espressif's ESP32 SoC.
- ports/nrf/ -- a version of MicroPython that runs on Nordic's nRF51 and nRF52 MCUs.
- extmod/ -- additional (non-core) modules implemented in C.
- tools/ -- various tools, including the pyboard.py module.
- examples/ -- a few example Python scripts.

The subdirectories above may include READMEs with additional info.

"make" is used to build the components, or "gmake" on BSD-based systems.
You will also need bash, gcc, and Python 3.3+ available as the command `python3`
(if your system only has Python 2.7 then invoke make with the additional option
`PYTHON=python2`).

The MicroPython cross-compiler, mpy-cross
-----------------------------------------

Most ports require the MicroPython cross-compiler to be built first.  This
program, called mpy-cross, is used to pre-compile Python scripts to .mpy
files which can then be included (frozen) into the firmware/executable for
a port.  To build mpy-cross use:

    $ cd mpy-cross
    $ make



External dependencies
---------------------

Building MicroPython ports may require some dependencies installed.

For Unix port, `libffi` library and `pkg-config` tool are required. On
Debian/Ubuntu/Mint derivative Linux distros, install `build-essential`
(includes toolchain and make), `libffi-dev`, and `pkg-config` packages.

Other dependencies can be built together with MicroPython. This may
be required to enable extra features or capabilities, and in recent
versions of MicroPython, these may be enabled by default. To build
these additional dependencies, in the port directory you're
interested in (e.g. `ports/unix/`) first execute:

    $ make submodules

This will fetch all the relevant git submodules (sub repositories) that
the port needs.  Use the same command to get the latest versions of
submodules as they are updated from time to time. After that execute:

    $ make deplibs

This will build all available dependencies (regardless whether they
are used or not). If you intend to build MicroPython with additional
options (like cross-compiling), the same set of options should be passed
to `make deplibs`. To actually enable/disable use of dependencies, edit
`ports/unix/mpconfigport.mk` file, which has inline descriptions of the options.
For example, to build SSL module (required for `upip` tool described above,
and so enabled by default), `MICROPY_PY_USSL` should be set to 1.

For some ports, building required dependences is transparent, and happens
automatically.  But they still need to be fetched with the `make submodules`
command.

The STM32 version
-----------------

The "stm32" port requires an ARM compiler, arm-none-eabi-gcc, and associated
bin-utils.  For those using Arch Linux, you need arm-none-eabi-binutils,
arm-none-eabi-gcc and arm-none-eabi-newlib packages.  Otherwise, try here:
https://launchpad.net/gcc-arm-embedded

To build:

    $ cd ports/stm32
    $ make submodules
    $ make

You then need to get your board into DFU mode.  On the pyboard, connect the
3V3 pin to the P1/DFU pin with a wire (on PYBv1.0 they are next to each other
on the bottom left of the board, second row from the bottom).

Then to flash the code via USB DFU to your device:

    $ make deploy

This will use the included `tools/pydfu.py` script.  If flashing the firmware
does not work it may be because you don't have the correct permissions, and
need to use `sudo make deploy`.
See the README.md file in the ports/stm32/ directory for further details.


The esp32 version
-----------------

    $ git clone https://github.com/micropython/micropython.git
    $ cd micropython

    $ git submodule update --init lib/axtls lib/berkeley-db-1.xx

    $ cd mpy-cross
    $ make
    $ cd ..

    $ cd ports/esp32/
    $ make USER_C_MODULES=user_modules/st7735_mpy/st7735/micropython.cmake

