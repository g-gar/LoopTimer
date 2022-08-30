# LoopTimer

Creating loops is where a lot of time is spent in every project. Testing, checking what it's doing, the time it spends on each iteration...

This project aims to remove that burden from our day to day by shipping full featured loops based on those most common patterns, just by writing a single line.

## Examples
Attempts to create a loop from `i=0` to `i=200` (exclusive) with a condition of `i < 20` and logging generated parameters for each iteration with a custom template:
```python
template = 'current iteration: index={index}'
Loop() \
  .index_generator(IterativeGenerator(0, 200, 2, lambda x: x < 20)) \
  .add_processor(LoggingProcessor()) \
  .run()
```

Same as before but `0 < i < 5, i+1` after executing `0 < i < 20, i+2`:
```python
template = 'current iteration: index={index}'
loop = Loop() \
  .index_generator(IterativeGenerator(0, 200, 2, lambda idx: idx < 20)) \
  .add_processor(LoggingProcessor(template)) \
  .run() \
  .index_generator(IterativeGenerator(0, 5, 1)) \
  .run()
```

## Next steps
- [ ] Execute processors taking its priority in account
- [ ] Bubble up processors generated values for other processors usage
- [ ] Introduce __execution flows__ (sync vs async, for example), that would be injected in `Loop.run()` or via its builder interface
- [x] Reset a Loop instance index generator function for reusability purposes
- [ ] Conditions in generators as `*args` for simplicity
- [ ] Add processors for function executions (chainable or multithreaded) as a `Loop.run()`'s `*arg` or via `**kwargs` (key could be the priority as well) argument