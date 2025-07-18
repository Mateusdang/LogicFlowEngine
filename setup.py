from setuptools import setup, find_packages

setup(
    name="pylogicator",
    version="0.1.0",
    description="Biblioteca profissional de lógica, automação de fluxos e dados para projetos em Python.",
    long_description=open("README.md", encoding="utf8").read(),
    long_description_content_type="text/markdown",
    author="Mateus Dang",
    author_email="mteus2030lol@gmail.com",
    packages=find_packages(),
    python_requires=">=3.8",
    url="https://github.com/Mateusdang/pylogicator",
    license="MIT",
    keywords="lógica automação python fluxo tabela verdade",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=[],
)