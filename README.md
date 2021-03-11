# CS362 In-Class Activity Week 10 - Continuous Integration
This activity tasked us with using CircleCI to develop a project with continous integration. To accomplish this, we integrated CircleCI with the calculator.py project from a previous in-class activity.

The image below showcases the output from running pytest --cov on the calculator.py and test_calculator.py pair.

![Pytest terminal output](https://github.com/lemossc/cs362-continuous-integration/blob/master/pytest-output.png)

CircleCI, after being integrated with the project, reruns the above test each time a commit is pushed to the repository. 

For example, I implmented a divide test to test_calculator.py, which failed since its method was not yet implemented. But once the method was implemented in calculator.py, the build succeeded. Below is an image of CircleCI's pipeline for this repository.

![CircleCI pipeline](https://github.com/lemossc/cs362-continuous-integration/blob/master/circleci-example.png)

This automates, to a degree, the testing portion of development, allowing developers to focus their attention elsewhere.
