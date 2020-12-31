# Derby benchmark

Derby benchmark is a simple tool to benchmark connections and queries to the
Derby database.

## Running

To run the app as-is, just run the following to get a full list of available
options.

```
docker run --rm --network host rokcarl/derby-benchmark /app/run.py -h
```

## Modifying and building

If you need additional functionality, do the following:

1. Change the Python code as needed.
2. `make build`.
3. `make run` or just run the above command.

## Example

For running this against two Derby databases to compare the results, run:

```
docker run --rm --network host rokcarl/derby-benchmark /app/run.py database_name "select * from customers" db1:9000 db2:9000
```