import argparse

from flatdb import flatdb_app
from flatdb.app import define_urls


def run_server():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--debug', action='store_true', default=False)
    parser.add_argument('-p', '--port', type=int, default=7532)
    parser.add_argument('-b', '--database')
    parser.add_argument('-H', '--host', default='127.0.0.1')
    options = parser.parse_args()
    flatdb_app.config['DB'] = options.database
    define_urls(flatdb_app)
    flatdb_app.run(debug=options.debug, port=options.port, host=options.host)


if __name__ == '__main__':
    run_server()
