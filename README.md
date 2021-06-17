# LoopTimer

Creating loops is where a lot of time is spent in every project. Testing, checking what it's doing, the time it spends on each iteration...

This project aims to remove that burden from our day to day by shipping full featured loops based on those most common patterns, just by writing a single line.

Moreover, every step on the loop generates enough information to create full featured benchmark reports.

A few examples (outputs are shown at the end of the document):

* `LoopTimer.run(lambda x: 2**x, 45)`

* `LoopTimer.run(lambda x: 2**x, 50, batch_size = 10)`

Disclaimer: `LoopTimer` interface will probably change substantially in prior versions

## External dependencies

None

## Features

| Loop type        | Phase | Stops  | Restarts | Pauses | Resumes | Jumps |
|:----------------:|:-----:|:------:|:--------:|:------:|:-------:|:-----:|
| Iteration        | 2     | almost | 2        | almost | 2       | 0     |
| Recursion        | 0     | 0      | 0        | 0      | 0       | 0     |
| Tail Recursion   | 0     | 0      | 0        | 0      | 0       | 0     |
| Divide & Conquer | 0     | 0      | 0        | 0      | 0       | 0     |
| Memoization      | 1     | 0      | 0        | 0      | 0       | 0     |

### Feature Phases

| Id  | Name                 | Descriptor                                                                                            |
|:---:|:--------------------:|:-----------------------------------------------------------------------------------------------------:|
| 0   | feature introduction | Feature has been introduced and it's in phase of approval                                             |
| 1   | prototyping          | Feature is being designed in order to fit with project's codebase (might introduce important changes) |
| 2   | testing              | Feature codebase is almost finished and it's in testing process to diminish future bugs               |
| 3   | launch               | Feature is part of the codebase and ready to use                                                      |

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