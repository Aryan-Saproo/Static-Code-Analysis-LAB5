# Reflection

## 1. Easiest vs. Hardest Issues to Fix

-   **Easiest fixes:**
    -   Renaming functions to use `snake_case` and removing the unused
        `logging` import were straightforward.\
    -   Adding docstrings and specifying `encoding="utf-8"` in file
        operations also required minimal effort.
-   **Hardest fixes:**
    -   Removing the global variable (`stock_data`) dependency was
        trickier since it required restructuring function logic to
        maintain data consistency.\
    -   Replacing `eval()` safely and introducing type validation
        without breaking existing behavior required careful thought.

------------------------------------------------------------------------

## 2. False Positives from Static Analysis

-   One potential **false positive** was the warning about the global
    variable.
    -   In this small-scale script, using a global `stock_data`
        dictionary is not inherently unsafe, though it's discouraged in
        larger systems.\
    -   The tool flagged it correctly in principle but contextually, it
        wasn't a functional issue here.

------------------------------------------------------------------------

## 3. Integration of Static Analysis Tools into Workflow

-   I would integrate static analysis tools in the following ways:
    -   **Local development:** Use `pylint` and `flake8` pre-commit
        hooks to automatically lint and block commits with critical
        issues.\
    -   **Continuous Integration (CI):** Configure tools like GitHub
        Actions or GitLab CI to run `pylint`, `bandit`, and `black` on
        every push or pull request.\
    -   **Automated code review:** Generate reports or badges showing
        code quality scores for transparency in team development.

------------------------------------------------------------------------

## 4. Tangible Improvements After Fixes

-   The code is now **more readable and maintainable** --- consistent
    naming and clear docstrings improve comprehension.\
-   **Safety and robustness** improved through proper exception
    handling, input validation, and safe file operations.\
-   **Maintainability** increased with structured design, reduced global
    reliance, and cleaner I/O practices.\
-   Overall, the fixes significantly enhanced code quality and lowered
    the risk of runtime or security issues.
