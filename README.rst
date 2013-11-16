======
FlatDB
======


FlatDB is a thin HTTP wrapper around LevelDB. LevelDB is a simple,
persistent key-value store.


API
===

There are three endpoints. Each accepts multiple values at a time. All
use HTTP GET. (This is not a RESTful interface.)


``/get``
--------

::

    GET /get?key=foo&key=bar HTTP/1.0

Get one or more values from the database. The response will be a JSON
object with a key for each ``key`` found in the database.


``/put``
--------

::

    GET /put?foo=bar&baz=qux HTTP/1.0

Store one or more values in the database. If multiple key/value pairs
are specified, they will be written atomically as a batch. If the write
succeeds, the return status will be 201. If the write fails, it will
not.


``/delete``
-----------

::

    GET /delete?key=foo&key=baz HTTP/1.0

Delete one or more keys from the database. If multiple keys are
specified, they will be deleted atomically as a batch. If the delete
succeeeds, the return status will be 200.


Why FlatDB?
===========

`LevelDB <http://leveldb.googlecode.com/svn/trunk/doc/index.html>`_ is
an ideal solution for a persistent, fast key-value store. (RocksDB is an
alternative from Facebook that has a lot in common, but is also very
new.) Since LevelDB (and RocksDB) is a library-level data store, FlatDB
provides a simple, service-oriented interface to it.

Other projects, like RevelDB and the Python leveldb-server package,
provide similar functionality, but:

* RevelDB barely built and then segfaulted on startup.
* leveldb-server is weird and tornadoy and undocumented.


Running FlatDB
==============

FlatDB is designed to run with gunicorn or the built-in Flask server.
The database is specified by the ``DB`` environment variable. For
example, in development::

    $ pip install -qr requirements.txt
    $ DB=test.db python flatdb.py -d

Or in production::

    $ gunicorn -b 127.0.0.1:7532 --env DB=test.db flatdb:app
