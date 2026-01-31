from setuptools import setup, find_namespace_packages

setup(
    name="clean_folder",
    version="0.0.1",
    description="Clean Folder Script",
    author="Pavlo F",
    license="MIT",
    packages=find_namespace_packages(),
    instal_requires=["markdown"],
    entry_points={"console_scripts": ["clean-folder = homework_1.homework_1:start"]}
)