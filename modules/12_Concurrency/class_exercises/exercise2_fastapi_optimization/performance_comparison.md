
## Results Comparison

**old version result:** <br>
Total Time: 30.95 seconds<br>
Average Response Time: 14.40 seconds<br>
Requests Per Second:0.65<br>



**new version result:**<br>
Total Time: 1.12 seconds<br>
Average Response Time: 17.42 seconds<br>
Requests Per Second:17.90<br>

***The improvement is actually impressive.***

**Total time:**<br>
(30.95 -1.12)/ 30.95 * 100<br>
=> decrease in total time 96.38% !!<br>

**Requests per second:**<br>
( 17.90 - 0.65)/ 0.65 * 100 <br>
=> increase in 2653% !!<br>

## Conclusion

The optimized version shows a dramatic improvement!!
This clearly demonstrates the impact of using AsyncIO and ProcessPoolExecutor for handling I/O bound and CPU bound tasks efficiently.