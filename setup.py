from setuptools import setup

setup(
    name='simple_text_editor',
    version='1.0',
    packages=[''],
    url='',
    license='MIT',
    author='',
    author_email='',
    description='A simple text editor using Tkinter',
    install_requires=[
        'tk',
    ],
    entry_points={
        'console_scripts': [
            'simple_text_editor = text_editor:main',
        ],
    },
    data_files=[('', ['icon.ico'])]
)
