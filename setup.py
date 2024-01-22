from setuptools import setup, find_packages

setup(
    name='voicestreamx',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # Add your project dependencies here
        'fastapi',
        'uvicorn',
        # Add other dependencies
    ],
    entry_points={
        'console_scripts': [
            'voicestreamx=app.main:main',
        ],
    },
)
