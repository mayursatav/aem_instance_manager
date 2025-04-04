from setuptools import setup, find_packages

setup(
    name="aem-instance-manager",
    version="0.1.0",
    author="Your Name",
    author_email="your-email@example.com",
    description="AEM Projects Instance Manager",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/aem-instance-manager",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "tkinter"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "aem-instance-manager = aem_instance_manager.main:main",
        ],
    },
)
