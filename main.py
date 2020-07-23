import os 

from common import run_blocking

tables_tpch = ["customer", "lineitem", "nation", "orders", "partsupp", "part", "region", "supplier"]
table_files = ["tpch-dbgen/{}.tbl".format(x) for x in tables_tpch]

print("Creating database generators")
run_blocking("cd tpch-dbgen && make")
run_blocking("cd ssb-dbgen && make")

sizes = {
    "small": 0.01,
    "med": 0.1,
    "big": 1,
    "huge": 2
}

folders = ("tpch-dbgen", "ssb-dbgen")
for folder in folders:
    makefile = "MakefileTPCH" if "tpc" in folder else "MakefileSSB"
    for size_name, scale_factor in sizes.items():
        env = os.environ.copy()
        env["SCALE_FACTOR"] = scale_factor

        print("Generating", folder, size_name, scale_factor)
        stdout, stderr = run_blocking("cd {} && rm *.tbl".format(folder))
        stdout, stderr = run_blocking("cd {} && ./dbgen -v -f -s {}".format(folder, scale_factor))
        print(stdout, stderr)
        stdout, stderr = run_blocking("make -f {}".format(makefile), env = env)
        print(stdout, stderr)
        run_blocking("mv TPC-H.db TPC-H-{}.db".format(size_name))
