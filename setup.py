from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

pkgs = find_packages(where='.')
print(pkgs)

setup(
    name='discord-verification-listener',
    version='1.0.0',
    description='A simple verification bot for discord',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Info-Bonn/verification-listener',
    author='nonchris',
    author_email='info@nonchris.eu',

    classifiers=[

        'Development Status :: 5 - Production/Stable',

        'Environment :: Console',

        'Intended Audience :: Other Audience',
        'Topic :: Communications :: Chat',

        'Typing :: Typed',

        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
    ],

    keywords='discord-bot, verification',

    package_dir={'': '.'},

    packages=find_packages(where='.'),

    python_requires='>=3.8, <4',

    install_requires='discord.py ~= 1.7.2',

    entry_points={  # Optional
        'console_scripts': [
            'verification-listener=src:main',
        ],
    },

    project_urls={  # Optional
        'Bug Reports': 'https://github.com/Info-Bonn/verification-listener/issues',
        'Source': 'https://github.com/Info-Bonn/verification-listener',
    },
)
