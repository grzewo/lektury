from pathlib import Path


def test_readme_exists():
    """
    Verify that a README file exists in the repository root.
    """
    # Check for common README file names
    readme_found = False
    for filename in ["README.md", "README"]:
        if Path(filename).exists():
            readme_found = True
            break
    assert readme_found, "README file not found in the repository root."
