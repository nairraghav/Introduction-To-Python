# Integration (Functional) Testing
Integration testing is, as the name suggests, testing the integration of various functions. If we have functions in various
python files that all come together to create one final product, the integration test will make sure the entire product
works holistically. Integration tests are extremely valuable to write but typically take more time in both creation and
runtime. You may wonder why we bother writing integration tests when we already have unit tests, look at the examples
below!

## Why We Should Write Integration Tests
When writing code, you may write the most perfect unit tests and they may ensure that every function within the program
works perfectly as expected. It may not be until they start working together that you realize something has gone wrong.
In the example below, both faucet and sink do their individual jobs. The faucet releases water and the sink is architecturally
sound to collect water and displace it. Unfortunately, the two were not tested to work together. They may work individually
but they fail as a whole. 
![integration-test-fail](../assets/lesson5-unit-test-integration-test-fail.gif)


Similar to the previous example, we can see that the door and lock would seem to pass their own individual tests. But
combining them results in something that may not have been caught. 
![integration-test-fail](../assets/lesson5-unit-test-integration-test-fail-2.gif) 


While both of the cases above may seem like hardware issues, this type of error is not unique to those fields. In fact,
these errors can occur frequently in software. If two separate develops are worth on two features that are to come together,
they may be fully in sync with how their individual features should behave holistically. Ideally, this should be handled
by whomever is architecting the solution but it is everyone's responsibility to make sure that the whole product can
function as a whole.

## Writing Integration Tests
When it comes to the implementation of the integration tests, they work just like unit tests. We still use pytest and
the specifics of naming conventions and pytest benefits still apply. The only difference now is the type of tests we are
writing. 

The goal of an integration test should be to test overall functionality not just an individual function. So if your program
takes in a file and outputs another file. Your integration test should have some sample input file and validate the output
is created and maybe even the data inside it.

\
\
\
\
[Up Next: Lesson 5 - Testing Example](testing-example/README.md)
\
\
\
[Go Back: Lessons 5 - Testing](README.md)