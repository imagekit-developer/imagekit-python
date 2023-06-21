# Development Guide

**1. Setup dependencies**

```shell
pip install -r requirements/requirements.txt
```

**2. Run test cases**

```shell
pip install -r requirements/test.txt
tox -e py
```

**3. Running the sample app**

```shell
pip install -r sample/requirements.txt
cd sample
python sample.py
```
## Contribution

We welcome contributions to enhance the project and appreciate your efforts! To contribute, please follow these steps:

```shell
# 1. Fork the repository using the 'Fork' button at the top of the repository page.
# 2. Clone your forked repository to your local machine:
git clone https://github.com/your-username/repository.git

# 3. Navigate to the project's root directory:
cd repository

# 4. Create a new branch for your contribution:
git checkout -b new-branch-name

# 5. Install the project dependencies, including 'pre-commit':
pip install -r requirements.txt

# 6. Install the pre-commit hooks:
pre-commit install

# 7. Make your desired changes and additions to the codebase.

# 8. Before committing your changes, ensure that the pre-commit hooks are automatically checking and formatting your code:
pre-commit run --all-files

# 9. Stage and commit your changes:
git add .
git commit -m "Your commit message"

# 10. Push your changes to your forked repository:
git push origin new-branch-name

# 11. Visit your forked repository on GitHub and create a pull request from your new branch to the original repository.

# 12. Your contribution will be reviewed, and if everything looks good, it will be merged into the main repository.

# 13. Thank you for your contribution!
