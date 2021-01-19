# if-else_alternatives
This is an educational purposed test, comparing if-elif-else statements with alternatives using a list, tuple and dictionary.

The program compares the average time of execution (absolute time) from an specific amount of repetitions on each coded alternative.
The time was measured using "time.perf_counter()"

## Test qualities:
* Each alternative consists of ten options compared with 0 to 9 values to choose an option.
* All options do the same operations. Initialization and declaration of a variable a, which receives the result of a constant sum operation: 1+1. Then it is added to itself.
* To allow the non if-elif-else alternatives each alternative is coded as a separated function (even if all do the same to allow more "real world" accuracy)
* For comparison reasons a version of the if-elif-else option where it doesn't use the function calls but instead it has the code directly in each option was implemented.


## Overall results:

The results where calculated running a million repetitions where each passed each and every value for the options (0 to 9) using two nested "for in range" loops.
These where run in a laptop with a 4-core Intel i7-6500U CPU with a 2.5GHz clock, with 12 GB of RAM.

Average Elapsed time (if statement):  6.6684908001871005e-06  With:  1000000  repetitions.

Average Elapsed time (if statement no function calls):  5.051403005728389e-06  With:  1000000  repetitions.

Average Elapsed time (constant list alternative):  4.3710357992858915e-06  With:  1000000  repetitions.

Average Elapsed time (created list alternative):  6.263405300115664e-06  With:  1000000  repetitions.

Average Elapsed time (constant tuple alternative):  4.2655419983630055e-06  With:  1000000  repetitions.

Average Elapsed time (created tuple alternative):  6.305673699903309e-06  With:  1000000  repetitions.

Average Elapsed time (constant dictionary alternative):  4.4364086998730274e-06  With:  1000000  repetitions.

Average Elapsed time (created dictionary alternative):  9.155623301213382e-06  With:  1000000  repetitions.

(For details on each, refer to the main.py file)
