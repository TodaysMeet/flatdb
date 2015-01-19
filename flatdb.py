import argparse
import leveldb
import os
import ujson as json
from flask import Flask, request, g


JSON = {'Content-Type': 'application/json'}
DB = os.getenv('DB')
app = Flask(__name__)


def ensure_db():
    if 'db' not in g:
        g.db = leveldb.LevelDB(DB)


@app.route('/put')
def put():
    ensure_db()
    keys = request.args.items(multi=True)
    batch = leveldb.WriteBatch()
    for k, v in keys:
        batch.Put(k, v)
    g.db.Write(batch)
    return '', 201, JSON


@app.route('/get')
def get():
    ensure_db()
    keys = request.args.getlist('key')
    if not keys:
        return '', 204, JSON
    response = {}
    for k in keys:
        try:
            response[k] = g.db.Get(k)
        except KeyError:
            pass
    if not response:
        return '', 404, JSON
    return json.dumps(response), 200, JSON


@app.route('/getrange')
def getrange():
    ensure_db()
    from_key = request.args.get('from')
    response = {}
    vals = g.db.RangeIter(key_from=from_key)
    for k, v in vals:
        response[k] = v
    if not response:
        return '', 404, JSON
    return json.dumps(response), 200, JSON


@app.route('/delete')
def delete():
    ensure_db()
    keys = request.args.getlist('key')
    batch = leveldb.WriteBatch()
    for k in keys:
        batch.Delete(k)
    g.db.Write(batch)
    return '', 200, JSON


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--debug', action='store_true', default=False)
    parser.add_argument('-p', '--port', type=int, default=7532)
    options = parser.parse_args()
    app.run(debug=options.debug, port=options.port)
