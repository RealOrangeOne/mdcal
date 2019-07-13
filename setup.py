from setuptools import setup

setup(
    name="mdcal",
    version="0.0.0",
    url="https://github.com/realorangeone/mdcal",
    author="Jake Howard",
    description="Generate a calendar feed from a series of markdown files ",
    packages=["mdcal"],
    python_requires=">=3.5",
    install_requires=["click==7.0"],
    project_urls={"GitHub: Issues": "https://github.com/realorangeone/mdcal/issues"},
    entry_points={"console_scripts": ["mdcal=mdcal.__main__:main"]},
)
