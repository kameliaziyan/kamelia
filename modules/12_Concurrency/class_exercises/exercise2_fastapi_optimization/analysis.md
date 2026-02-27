
# Analyze and Measure Current Performance <br><br>
## Test results

 After running a single request I got the following result: <br>
**time = 1.560 second**

#### Also when I ran 20 requests using load_test.py these were the results:

Total Time: 31.01 seconds. <br>
Average Response Time: 14.41 seconds <br>
Requests Per Second:0.65 <br>
python load_test.py  0.15s user 0.02s system 0% cpu 31. <br>
166 total

#### so the given code is not good enough, and for sure there is a way to improve it and make it work faster and better.

After checking the code, this is my opinion on what we can do to improve it 

## Some ideas to improve the code


1. we can fix the Fibonacci function

    Its slow and blocks the server. We can make it faster or move it to a separate process.


2. we can replace time.sleep with async sleep


    It blocks everything. We can use **asyncio.sleep()** insted


3. we can run the data fetching functions together


    Right now they run one by one. We can use **asyncio.gather()** to run them at the same time.


4. we can improve the payment simulation


   It also blocks the server, so we should change it to to async.










