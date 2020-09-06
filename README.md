# LLVMSQLite_DBGen

This repository is almost an exact copy from [https://github.com/lovasoa/TPCH-sqlite](https://github.com/lovasoa/TPCH-sqlite). 

It only removes TPCH-DBGen as a submodule (to include the code directly) and adds the SSBM-DBGen source. 

The Makefile has been duplicated and slightly modify to allow generating both TPC-H and SSBM databases. 
To use it, do the following:

```
make -f MakefileSSBM
make -f MakefileTPCH
```

All implementation credits go to [https://github.com/lovasoa/TPCH-sqlite](https://github.com/lovasoa/TPCH-sqlite). 
TPC-H DBGen and SSBM DBGen sources are included as allowed by their licenses. 
