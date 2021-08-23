# training-material

A collection of code examples for training purposes, mostly in the
context of data processing and parallel programming.

This material is made available as is, i.e., anyone is welcome to use it,
and to [contribute](CONTRIBUTING.md).  However, no support is guaranteed
in any form.  All material is subject to the [license](LICENSE) included
in this repository.

Tips and tricks can be found on this [repository's website](http://gjbex.github.io/training-material/).

[![DOI](https://www.zenodo.org/badge/18587808.svg)](https://www.zenodo.org/badge/latestdoi/18587808)


## What is it?

* [`Accelerators`](Accelerators): some sample code and information on using
   accelerators.
* [`C`](C): presentation based "The C programming language" by Kernighan and
   Ritchie, as well as sample code to illustration the concepts.
* [`CPlusPlus`](CPlusPlus): presentation based on "A tour of C++" by Stroustrup,
    as well as sample code to illustrate the concepts.
* [`DataStorage`](DataStorage): sample code showing how to read/write HDF5 and
    NetCDF files from C, Fortran, and Python.  HDF5 can be used for parallel
    I/O, C sample code is provided.  The HDF5 material is part of a tutorial on
    that subject.  Sample code on how to interact with a redis data
    structure server is also provided, illustrating the hiredis C API.
    Sample SQL covers the basics of querying relational databases
* [`Debugging`](Debuggers): slides used for an info session on debugging tools
   and techniques, as well as sample code.
* [`Fortran`](Fortran): presentation on "Modern Fortran" as well sample code
    intended to illustrate Fortran 95, 2003, and 2008 features.
* [`Java`](Java): sample code mostly for demonstration purposes.
* [`LinuxTools`](LinuxTools): some illustrations of using Linux tools such as
    the `M4`macro processor, make files and autotools, as well as slides on
    version control using svn and git.
* [`Math`](Math): sample code for using various mathematical libraries.
* [`Misc`](Misc): catch-all for one-time presentations, or special sessions.
* [`Mpi`](Mpi): illustration of distributed programming using the Message
    Passing Interface API.
* [`OpenMP`](OpenMP): sample code for OpenMP.
* [`Optimization`](Optimization): illustrations of performance optimization
   opportunities.
* [`PBS`](PBS): sample PBS torque batch scripts to illustrate features.
* [`Python`](Python): sample code to explore various Python features, standard
    library packages and third party libraries.  Most of this material is
    used in a tutorial on using Python for scientific data processing.
* [`R`](R): some very simple illustrations of how to run R scripts from the
    command line, and to submit as (PBS) jobs
* [`Virtualization`](Virtualization): Information on how to use Singularity.
    (Work in progress)
* [`Visualization`](Visualization): data files, XDMF files and ParaView state
    files to use during a demo of scientific visualization with ParaView.


## Contributors

* Geert Jan Bex ([geertjan.bex@uhasselt.be](mailto:geertjan.bex@uhasselt.be)),
  Hasselt University/University of Leuven
* Stefan Becuwe, University of Antwerp
  * suggestions for and correction of typos in Python presentation
  * suggestions for Python programming exercises
* Guillaume Jacquenot
  * Python 3 version of XDMF generating scripts
  * correcting typos in various README
  * suggesting hyperlinking the README files, and providing a Python script for
    it
* Arnout Standaert, VITO
  * update of deprecated Pandas API
  * suggestions on Python OOP presentation section
* Yana Maneva, KU Leuven
  * suggestions on online C++ training material references


You are very welcome to contribute, please read
[some guidelines](CONTRIBUTING.md) before you do.
