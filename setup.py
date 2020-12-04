from setuptools import setup, find_packages  # type:ignore

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
   name='gva.services',
   version='0.0.1',
   description='GVA Services',
   long_description=long_description,
   long_description_content_type="text/markdown",
   author='390516',
   author_email='justin.joyce@lloydsbanking.com',
   packages=find_packages(),
   url="https://github.com/gva-jjoyce/gva_data_flows",
   install_requires=['google.cloud', 'gva.data.flows']
)