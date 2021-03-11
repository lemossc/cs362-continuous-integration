# CS362 In-Class Activity Week 10 - Continuous Integration
This activity tasked us with using CircleCI to develop a project with continous integration. To accomplish this, we integrated CircleCI with the calculator.py project from a previous in-class activity.

The image below showcases the output from running pytest --cov on the calculator.py and test_calculator.py pair.

![Pytest terminal output](https://github.com/lemossc/cs362-continuous-integration/blob/master/pytest-output.png)

CircleCI, after being integrated with the project, reruns the above test each time a commit is pushed to the repository. This automates, to a degree, the testing portion of development, allowing developers to focus their attention elsewhere.
