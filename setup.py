from setuptools import setup

setup(
    use_scm_version={"write_to": "src/__version__.py"},
    setup_requires=["setuptools-scm"],
)
