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
