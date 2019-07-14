from setuptools import setup

setup(
    name="mdcal",
    version="0.0.0",
    url="https://github.com/realorangeone/mdcal",
    author="Jake Howard",
    description="Generate a calendar feed from a series of markdown files ",
    packages=["mdcal"],
    python_requires=">=3.5",
    install_requires=[
        "click==7.0",
        "python-dateutil==2.8.0",
        "ics==0.4",
        "markdown==3.1.1",
        "jinja2==2.10.1",
        "ruamel.yaml==0.15.99",
    ],
    project_urls={"GitHub: Issues": "https://github.com/realorangeone/mdcal/issues"},
    entry_points={"console_scripts": ["mdcal=mdcal.__main__:main"]},
)
