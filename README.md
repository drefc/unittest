# unittest

Source: https://docs.python.org/3/library/unittest.html

## test fixture

- **Preparation** needed to perform one or more tests, and any associated **cleanup actions**. This may involve, for example, **creating temporary** or proxy databases, directories, or **starting a server process**.

## test case

- A test case is the **individual unit of testing**. It checks for a specific response to a particular set of inputs. **unittest provides a base class, TestCase**, which may be used to create new test cases.
- It should be self contained.

## test suite

- A test suite is a **collection of test cases, test suites, or both**. It is used to **aggregate tests** that should be executed together.
- Test suites are automatically managed when unittest is called. However, it is also possible to use `unittest.TestSuite()` class, manually add the cases and call the runner to do so. It is a bit advanced though.
- It is encouraged to keep the all the tests in the same module of the code they are to test.

## test runner

- A test runner is a **component which orchestrates the execution of tests** and provides the outcome to the user. The runner may use a graphical interface, a textual interface, or return a special value to indicate the results of executing the tests.