<<<<<<< HEAD
# Compute Benchmark Results

## System Info

- **OS:** Linux 6.6.87.2-microsoft-standard-WSL2
- **Processor:** x86_64

## Benchmark Results

- **Execution Time:** 4.3740 seconds

## System Memory

- **Total RAM:** 12GB
=======
==================================================
SYSTEM INFORMATION
==================================================
OS:         Linux 6.6.87.2-microsoft-standard-WSL2
Version:    #1 SMP PREEMPT_DYNAMIC Thu Jun  5 18:30:46 UTC 2025
Machine:    x86_64
Processor:  x86_64
Python:     3.10.12 (main, Jan 26 2026, 14:55:28) [GCC 11.4.0]

Benchmark 1 — sum(range(5,000,000))
  Result:  12,499,997,500,000
  Time:    0.1158 seconds

Benchmark 2 — list comprehension (n=1,000,000)
  First 5: [0, 1, 4, 9, 16]
  Time:    0.1533 seconds

Benchmark 3 — string join (n=100,000)
  Length:  588,889 characters
  Time:    0.0201 seconds

==================================================
SUMMARY
==================================================
  sum benchmark:    0.1158s
  list benchmark:   0.1533s
  string benchmark: 0.0201s

Copy this output into docs/compute-log.md
Add your total RAM at the bottom of that file.

## RAM

Total RAM: 6 GB
>>>>>>> b6ba2e5 (PR 4: benchmark log + three bug fixes)
