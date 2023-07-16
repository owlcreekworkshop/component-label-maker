# Testing Guide

This guide provides instructions on writing and running tests for the [Component Label Maker](https://github.com/owlcreekworkshop/component-label-maker) project.

## Table of Contents
- [Running Tests](#running-tests)
- [Writing Tests](#writing-tests)
- [Test Coverage](#test-coverage)
- [Test Policy](#test-policy)

## Running Tests

  1. Make sure you have followed the installation steps mentioned in [README](README.md#installion).

  2. From the project's root directory, run the following command to execute all tests:

    $ pytest

  3. pytest will automatically discover and run all test files that follow the naming convention: `test_*.py` or `*_test.py`.

  4. Review the test results displayed in the terminal.

## Writing Tests

Please conform to the existing pattern of putting tests in the `/tests` subdirectory.

  1. Create a new test file or navigate to an existing one.

  2. Import necessary modules and functions for testing.

  3. Define test functions starting with `test_` to be discovered by pytest.

  4. Write test cases using assertions to verify expected behavior.

  5. Run the tests using the instructions mentioned in the "Running Tests" section.

Example test file (`test_example.py`):

    import my_module

    def test_addition():
        assert my_module.add(2, 3) == 5

    def test_subtraction():
        assert my_module.subtract(5, 3) == 2


## Test Coverage

Test coverage helps assess how much of your code is being tested. To measure the test coverage of your project:

  1. Make sure you have followed the installation steps mentioned above.

  2. From the project's root directory, run the following command:

    $ pytest --cov=labelmaker


  3. pytest will execute the tests and display the coverage report, including the percentage of code covered.

  4. Review the coverage report to identify areas of the code that may need additional tests.

## Test Policy

Before opening a pull request, it is mandatory that all tests are passing. Pull requests with failing tests will not be accepted. Make sure to run the tests locally and confirm that they pass before submitting your pull request.