#!/usr/bin/env python3
"""
Usage:
  run.py <database_name> <query> <db_host_port>... [--iterations <iterations>] [--sleep <sleep>]

Options:
  -h --help                  Show this screen.
  <database_name>            Name of the database.
  <query>                    The query to run for benchmarking.
  <db_host_port>...          The host and port for the database, can supply many, e.g. db1:9000 db2:9000.
  --iterations <iterations>  How many iterations of the test do you want to run. [default: 100].
  --sleep <sleep>            How many seconds to sleep between each iterations. [default: 0.1].
"""

from docopt import docopt
import drda
import numpy as np
import time
from timeit import default_timer as timer


def time_select_all(db_host, db_name, query, db_port, include_connection):
    if include_connection:
        start = timer()
    conn = drda.connect(
        host=db_host, database=db_name, use_ssl=True, port=db_port)
    cur = conn.cursor()
    if not include_connection:
        start = timer()
    cur.execute(query)
    cur.fetchall()
    if not include_connection:
        end = timer()
    cur.close()
    conn.close()
    if include_connection:
        end = timer()
    return end - start


def run(settings):
    sleep = float(settings["--sleep"])
    iterations = int(settings["--iterations"])
    db_name = settings["<database_name>"]
    query = settings["<query>"]
    for db_host_port in settings["<db_host_port>"]:
        db_host, port_str = db_host_port.split(":")
        port = int(port_str)

        print(f"Stats for {db_host}:\n")
        for include_connection in [True, False]:
            durations = []
            for _ in range(iterations):
                d = time_select_all(db_host, db_name, query, port, include_connection)
                durations.append(d)
                time.sleep(sleep)
            print(f"  Time stats ({'including' if include_connection else 'excluding'}) connection:")
            print(f"  Average:         {np.average(durations):.4f}s")
            print(f"  50th percentile: {np.percentile(durations, 50):.4f}s")
            print(f"  90th percentile: {np.percentile(durations, 90):.4f}s")
            print("")


if __name__ == "__main__":
    settings = docopt(__doc__)
    run(settings)
