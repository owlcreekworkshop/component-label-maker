
# Contributing Guide

Thank you for your interest in contributing to [Component Label Maker](https://github.com/owlcreekworkshop/component-label-maker). To get started, please review the guidelines below.

## Table of Contents
- [Code of Conduct](#code-of-conduct)
- [How to Contribute](#how-to-contribute)
- [Reporting Issues](#reporting-issues)
- [Submitting Pull Requests](#submitting-pull-requests)
- [Development Setup](#development-setup)
- [Style Guide](#style-guide)
- [Testing](#testing)
- [Documentation](#documentation)
- [Contact](#contact)
- [License](#license)

## Code of Conduct

Please read and adhere to our [Code of Conduct](CODE_OF_CONDUCT.md) to ensure a respectful and inclusive environment for all contributors.

## How to Contribute

Before starting your contribution, you should first open an issue to discuss and receive feedback on your proposed changes. This enables us to align our goals and make the most out of your contributions.

  1. Fork the repository and clone it locally.

  2. Create a new branch for your feature or bug fix: `git checkout -b my-feature-branch`.

  3. Make your changes, ensuring they follow the project's guidelines.

  4. Commit your changes with descriptive commit messages: `git commit -m "Add feature XYZ"`.

  5. Push your branch to your forked repository: `git push origin my-feature-branch`.

  6. Submit a pull request to the main repository's `main` branch, including a detailed description of your changes.

## Reporting Issues

If you encounter any issues or have suggestions for improvements, please [open an issue](https://github.com/owlcreekworkshop/component-label-maker/issues) and provide as much detail as possible. Include steps to reproduce the problem if applicable.

## Submitting Pull Requests

We encourage pull requests to address bugs, add new features, or improve documentation. Follow these steps to submit a pull request:

  1. Ensure your branch is up to date with the main repository.
  
  2. Include tests for any new features or bug fixes.
  
  3. Provide a clear and descriptive title for your pull request.
  
  4. Explain the motivation and impact of your changes in the description.
  
  5. Request reviews from project maintainers.
  
  6. Address any feedback or change requests from reviewers.
  
  7. Once approved, the pull request will be merged into the main repository.

## Development Setup

To set up the project for development, follow the instructions in the [README](README.md) file. It contains information about prerequisites, installation, and configuration.

Once that has been completed you will want to install the development dependencies: `pip install -r requirements_dev.txt`.

## Style Guide

Please follow [PEP 8](https://peps.python.org/pep-0008/) style guidelines when writing code for this project. Consistent coding style helps maintain readability and improves collaboration.

It is also recommended to run any changes through the configured linter prior to committing. Such as: `flake8 labelmaker/ tests/`

## Testing

Before submitting a pull request, make sure all existing tests pass and add new tests if necessary. Refer to the [Testing Guide](TESTING.md) for instructions on running tests.

## Documentation

Improving documentation is highly appreciated. The documentation for this project is simply part of the [README](README.md). Feel free to update existing documentation or add new sections to help users understand and use the project effectively.

## Contact

If you have any questions or need further assistance, you can reach out to us by opening an issue on GitHub.

# License

By contributing to this project, you agree that your contributions will be licensed under the [LICENSE](LICENSE) of the project.
