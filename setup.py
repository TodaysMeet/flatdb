from setuptools import setup, find_packages

install_requires = [
    'flask==0.10.1',
    'leveldb==0.19',
    'gevent==1.0.1',
    'ujson==1.33',
]


setup(
    name='flatdb',
    version='0.1.0',
    description='HTTP access to a LevelDB.',
    long_description=open('README.rst').read(),
    author='James Socol',
    author_email='james@todaysmeet.com',
    url='https://github.com/todaysmeet/flatdb',
    license='Apache Software License',
    packages=find_packages(),
    include_package_data=True,
    package_data={'': ['README.rst']},
    entry_points={
        'console_scripts': [
            'flatdb-dev = flatdb.run:dev_server',
            'flatdb = flatdb.run:run_server',
        ],
    },
    zip_safe=False,
    install_requires=install_requires,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
)
