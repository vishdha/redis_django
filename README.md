Install Redis
The first step is to get Redis up and running locally on your machine. The simplest way to install Redis is via the operating system’s package manager like so:


```
1.sudo apt-get install redis-server
```

To check if the redis server is running, issue the following command on the terminal:

```
1.$ sudo redis-server
2.* Ready to accept connections
```

To test load
Installing loadtest as root is simple:

```
1.sudo npm install -g loadtest
```

```
$ loadtest -n 100 -k  http://localhost:8000/store/

 loadtest -n 100 -k  http://localhost:8000/store/
[Wed May 18 2022 15:12:16 GMT+0530 (India Standard Time)] INFO Requests: 0 (0%), requests per second: 0, mean latency: 0 ms
[Wed May 18 2022 15:12:17 GMT+0530 (India Standard Time)] INFO 
[Wed May 18 2022 15:12:17 GMT+0530 (India Standard Time)] INFO Target URL:          http://localhost:8000/store/
[Wed May 18 2022 15:12:17 GMT+0530 (India Standard Time)] INFO Max requests:        100
[Wed May 18 2022 15:12:17 GMT+0530 (India Standard Time)] INFO Concurrency level:   1
[Wed May 18 2022 15:12:17 GMT+0530 (India Standard Time)] INFO Agent:               keepalive
[Wed May 18 2022 15:12:17 GMT+0530 (India Standard Time)] INFO 
[Wed May 18 2022 15:12:17 GMT+0530 (India Standard Time)] INFO Completed requests:  100
[Wed May 18 2022 15:12:17 GMT+0530 (India Standard Time)] INFO Total errors:        0
[Wed May 18 2022 15:12:17 GMT+0530 (India Standard Time)] INFO Total time:          1.3675151799999998 s
**[Wed May 18 2022 15:12:17 GMT+0530 (India Standard Time)] INFO Requests per second: 73
[Wed May 18 2022 15:12:17 GMT+0530 (India Standard Time)] INFO Mean latency:        13.6 ms**
[Wed May 18 2022 15:12:17 GMT+0530 (India Standard Time)] INFO 
[Wed May 18 2022 15:12:17 GMT+0530 (India Standard Time)] INFO Percentage of the requests served within a certain time
[Wed May 18 2022 15:12:17 GMT+0530 (India Standard Time)] INFO   50%      4 ms
[Wed May 18 2022 15:12:17 GMT+0530 (India Standard Time)] INFO   90%      46 ms
[Wed May 18 2022 15:12:17 GMT+0530 (India Standard Time)] INFO   95%      47 ms
[Wed May 18 2022 15:12:17 GMT+0530 (India Standard Time)] INFO   99%      51 ms
[Wed May 18 2022 15:12:17 GMT+0530 (India Standard Time)] INFO  100%      51 ms (longest request)
```

```
$ loadtest -n 100 -k  http://localhost:8000/store/cache/

[Wed May 18 2022 15:16:26 GMT+0530 (India Standard Time)] INFO Requests: 0 (0%), requests per second: 0, mean latency: 0 ms
[Wed May 18 2022 15:16:27 GMT+0530 (India Standard Time)] INFO 
[Wed May 18 2022 15:16:27 GMT+0530 (India Standard Time)] INFO Target URL:          http://localhost:8000/store/cache
[Wed May 18 2022 15:16:27 GMT+0530 (India Standard Time)] INFO Max requests:        100
[Wed May 18 2022 15:16:27 GMT+0530 (India Standard Time)] INFO Concurrency level:   1
[Wed May 18 2022 15:16:27 GMT+0530 (India Standard Time)] INFO Agent:               keepalive
[Wed May 18 2022 15:16:27 GMT+0530 (India Standard Time)] INFO 
[Wed May 18 2022 15:16:27 GMT+0530 (India Standard Time)] INFO Completed requests:  100
[Wed May 18 2022 15:16:27 GMT+0530 (India Standard Time)] INFO Total errors:        0
[Wed May 18 2022 15:16:27 GMT+0530 (India Standard Time)] INFO Total time:          0.684389826 s
**[Wed May 18 2022 15:16:27 GMT+0530 (India Standard Time)] INFO Requests per second: 146
[Wed May 18 2022 15:16:27 GMT+0530 (India Standard Time)] INFO Mean latency:        6.8 ms**
[Wed May 18 2022 15:16:27 GMT+0530 (India Standard Time)] INFO 
[Wed May 18 2022 15:16:27 GMT+0530 (India Standard Time)] INFO Percentage of the requests served within a certain time
[Wed May 18 2022 15:16:27 GMT+0530 (India Standard Time)] INFO   50%      1 ms
[Wed May 18 2022 15:16:27 GMT+0530 (India Standard Time)] INFO   90%      45 ms
[Wed May 18 2022 15:16:27 GMT+0530 (India Standard Time)] INFO   95%      46 ms
[Wed May 18 2022 15:16:27 GMT+0530 (India Standard Time)] INFO   99%      49 ms
[Wed May 18 2022 15:16:27 GMT+0530 (India Standard Time)] INFO  100%      49 ms (longest request)


Reference: https://code.tutsplus.com/tutorials/how-to-cache-using-redis-in-django-applications--cms-30178

above link contain old code so this repo contain refactored and updated version to learn more about redis..