from distutils.core import setup
setup(
    name="cofactr",
    packages=["cofactr"],
    version="0.0.1",
    description="Client library for accessing Cofactr data.",
    url="https://github.com/Cofactr/cofactr-client",
    download_url="https://github.com/Cofactr/cofactr-client/archive/refs/tags/0.0.1.tar.gz",
    author="Cofactr",
    author_email="noah@cofactr.com, riley@cofactr.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    install_requires=[
      "urllib3",
    ],
)