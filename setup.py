from setuptools import setup, find_packages

setup(
    name="ETLpipelineXiYueZhang",
    version="0.1.0",
    description="ETLpipline",
    author="Xiyue Zhang",
    author_email="xiyue.zhang@duke.edu",
    packages=find_packages(),
    install_requires=[
        "mysql-connector-python",
        "pandas",
        "python-dotenv",
    ],
    entry_points={
        "console_scripts": [
            "etl_query=main:main",
        ],
    },
)
