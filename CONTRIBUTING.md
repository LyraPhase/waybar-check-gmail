<!-- markdownlint-configure-file
{
  "line-length": true,
  "required-headings": {
    "headings": [
      "# Contributing",
      "## Types of Contributions",
      "### Report Bugs",
      "*",
      "### Fix Bugs",
      "*",
      "### Implement Features",
      "*",
      "### Write Documentation",
      "*",
      "### Submit Feedback",
      "*",
      "## Get Started",
      "*",
      "## Pull Request Guidelines",
      "*"
    ]
  }
}
-->

# Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

You can contribute in many ways:

## Types of Contributions

### Report Bugs

Report bugs at <https://github.com/LyraPhase/waybar-check-gmail/issues>.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

### Fix Bugs

Look through the GitHub issues for bugs. Anything tagged with "`bug`"
and "`help wanted`" is open to whoever wants to implement it.

### Implement Features

Look through the GitHub issues for features. Anything tagged with "`enhancement`"
and "`help wanted`" is open to whoever wants to implement it. Those that are
tagged with "`first-timers-only`" is suitable for those getting started in
open-source software.

### Write Documentation

The project could always use more documentation, whether as part of the
official docs, in docstrings, or even on the web in blog posts,
articles, and such.

### Submit Feedback

The best way to send feedback is to file an issue at <https://github.com/LyraPhase/waybar-check-gmail/issues>.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a **_volunteer-driven_** project, and that contributions
  are welcome 😊 🙏

## Get Started

Ready to contribute? Here's how to set up `waybar-check-gmail` for local development.

1. Fork the `waybar-check-gmail` repo on GitHub.
2. Clone your fork locally:

    git clone git@github.com:your_name_here/waybar-check-gmail.git

3. Install your local copy into a [virtualenv][1].
   Assuming you have [virtualenvwrapper installed][2],
   this is how you set up your fork for local development:

      mkvirtualenv waybar-check-gmail
      cd waybar-check-gmail/
   &nbsp;<!-- TODO: Implement/document python-poetry -->
   <!-- TODO: python setup.py develop vs. poetry command -->

4. Create a branch for local development:

      git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

5. When you're done making changes, check that they pass [`flake8`][3] and the
   tests, including testing other Python versions with [`tox`][4].
   In addition, ensure that your code is formatted using [`black`][5]:

    flake8 waybar-check-gmail tests
    black waybar-check-gmail tests
    python setup.py test # or py.test
    tox

   To get [`isort`][6], [`flake8`][3], [`flake8-isort`][7], [`black`][5],
   [`bandit`][9], [`pytest`][10], and [`tox`][4],
   just `pip install` them into your [`virtualenv`][1].

      pip install -r requirements-dev.txt

   Alternatively, you may install these via your OS package manager but beware
   that versions may not match those in CI/CD.
   You may also add [`pre-commit`][8] hooks for both `flake8` and `black` to make
   all formatting easier.  This is the method that the CI/CD pipelines use, and
   so is most easily replicated.

      pre-commit install

   Finally, to test multiple python versions you will need to install multiple
   versions side-by-side.  The easiest way to do this is to use [`pyenv`][12],
   and [`python-build`][13].  Note that `python-build` is installed by default
   with `pyenv`, but your OS may have this as a separate package.
   To install the versions of python this project is using:

      cat .python-version | sed -e '/^system/d' | tr '\n'  ' ' \
      | xargs pyenv install

   Alternatively, you may [select and install some other versions][14].

6. Commit your changes and push your branch to GitHub:

    git add .
    git commit -m "Your detailed description of your changes."
    git push origin name-of-your-bugfix-or-feature

   In brief, commit messages should follow these conventions:

   * Always contain a subject line which briefly describes the changes made.
   For example "Update CONTRIBUTING.md".
     * For new features, use prefix: `feat:`
     * For bugfixes, use prefix: `fix:`
       * [Link your commit message to the issue number][github-link-issues]
   * Subject lines should ideally not exceed 50-72 characters.
   * The commit body should contain context about the change - how the code
     worked before, how it works now and
     why you decided to solve the issue in the way you did.

   More detail on commit guidelines can be found at
   * [cbeams - How to Write a Git Commit Message][cbeams-git-commit]

7. Submit a pull request through the GitHub website.

## Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.md.
3. The pull request should work for Python 3.4, 3.5, and above. Check
   <https://github.com/LyraPhase/waybar-check-gmail/actions>
   and make sure that the tests pass for all supported Python versions.

[1]: https://virtualenv.pypa.io/en/latest/
[2]: https://virtualenvwrapper.readthedocs.io/en/latest/install.html
[3]: https://github.com/PyCQA/flake8
[4]: https://tox.wiki/en/4.7.0/
[5]: https://black.readthedocs.io/en/stable/
[6]: https://pycqa.github.io/isort/
[7]: https://github.com/gforcada/flake8-isort
[8]: https://pre-commit.com/
[9]: https://bandit.readthedocs.io/en/latest/
[10]: https://tox.wiki/en/3.27.0/example/pytest.html
[12]: https://github.com/pyenv/pyenv#installation
[13]: https://github.com/pyenv/pyenv/tree/master/plugins/python-build
[14]: https://coderwall.com/p/vj2jxg/select-install-python-versions-easily-with-fzf

<!-- TODO: Implement/document python-poetry -->
<!-- [11]: https://hackersandslackers.com/python-poetry-package-manager/ -->

[cbeams-git-commit]: https://chris.beams.io/posts/git-commit
[github-link-issues]: https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue#linking-a-pull-request-to-an-issue-using-a-keyword
