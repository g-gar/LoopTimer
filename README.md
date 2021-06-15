# LoopTimer
Helper for benchmarking loops

## External dependencies
None

## Examples

* `LoopTimer.run(lambda x: 2**x, 45, batch_size = 10)`
```
iteration = 0    took 0.00000000s        total = 0.00000000s     value = 1
iteration = 10   took 0.00000000s        total = 0.00000000s     value = 1024
iteration = 20   took 0.00000000s        total = 0.00000000s     value = 1048576
iteration = 30   took 0.00000000s        total = 0.00000000s     value = 1073741824
iteration = 40   took 0.00000000s        total = 0.00000000s     value = 1099511627776
```

* `LoopTimer.run(lambda x: 2**x, 50, batch_size = 10)`
```
iteration = 0    took 0.00000000s        total = 0.00000000s     value = 1
iteration = 10   took 0.00000000s        total = 0.00000000s     value = 1024
iteration = 20   took 0.00000000s        total = 0.00000000s     value = 1048576
iteration = 30   took 0.00000000s        total = 0.00000000s     value = 1073741824
iteration = 40   took 0.00000000s        total = 0.00000000s     value = 1099511627776
iteration = 50   took 0.00000000s        total = 0.00000000s     value = 1125899906842624
```