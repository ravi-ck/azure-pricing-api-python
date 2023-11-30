from setuptools import find_packages, setup

setup(
    name="azure_pricing_api",
    version="1.1.0",
    description="Python SDK to leverage Azure Pricing API",
    url="https://github.com/ravi-ck/azure-pricing-api-python",
    author="Ravi Rana",
    author_email="ravi.rana@tothenew.com",
    license="Apache-2.0 license",
    package_dir={"": "azure_pricing_api"},
    packages=find_packages(where="azure_pricing_api"),
    install_requires=[
        "requests==2.31.0"
    ]
)