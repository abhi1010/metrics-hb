# Metrics

- [Source](https://github.com/prometheus/client_python)
- [best article on counter/summary/histogram](https://pierrevincent.github.io/2017/12/prometheus-blog-series-part-2-metric-types/)
- [Histograms in-depth](http://linuxczar.net/blog/2017/06/15/prometheus-histogram-2/)


Run

```bash
source ~/apps/code/githubs/abhi1010/prometheus-tuts/ve/bin/activate
which python
python prom.py
```
Access at `http://localhost:8000`


## Prom

`prometheus --config.file=prom.yml`


### Samples

```
avg(rate(request_processing_seconds_count[1m])) by (job, service)
```

## Results

This looks something like:

```log
# HELP process_virtual_memory_bytes Virtual memory size in bytes.
# TYPE process_virtual_memory_bytes gauge
process_virtual_memory_bytes 441548800.0
# HELP process_resident_memory_bytes Resident memory size in bytes.
# TYPE process_resident_memory_bytes gauge
process_resident_memory_bytes 20131840.0
# HELP process_start_time_seconds Start time of the process since unix epoch in seconds.
# TYPE process_start_time_seconds gauge
process_start_time_seconds 1525673216.73
# HELP process_cpu_seconds_total Total user and system CPU time spent in seconds.
# TYPE process_cpu_seconds_total counter
process_cpu_seconds_total 0.19
# HELP process_open_fds Number of open file descriptors.
# TYPE process_open_fds gauge
process_open_fds 7.0
# HELP process_max_fds Maximum number of open file descriptors.
# TYPE process_max_fds gauge
process_max_fds 1024.0
# HELP python_info Python platform information
# TYPE python_info gauge
python_info{implementation="CPython",major="3",minor="6",patchlevel="4",version="3.6.4"} 1.0
# HELP request_processing_seconds Time spent processing request
# TYPE request_processing_seconds summary
request_processing_seconds_count 30.0
request_processing_seconds_sum 13.410392665999098
```

## How to run them

**Run Prometheus**
`prometheus --config.file=prom.yml`

**Run alertmanager**
`alertmanager`

**Run Python alert Receiver**
`python receiver.py`

**Run sample bot**
`python prom.py`

