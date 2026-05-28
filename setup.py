from setuptools import setup, find_packages

setup(
    name="ipc-quantum-core",
    version="1.0.0",
    packages=find_packages(),
    install_packages=[
        "fastapi==0.128.8",
        "uvicorn==0.39.0",
        "pydantic==2.13.4"
    ],
    author="emu1ua2enHsa",
    description="Information-Preserving Calculus multi-disciplinary computing core pipeline.",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS :: MacOS X",
    ],
)

