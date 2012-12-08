from setuptools import setup, find_packages

setup(name='djangoappengine_rdbms',
    version='0.0.1',
    description='Django SQL backend',
    author='Daniel Petrikin',
    author_email='dan@blackbeltprogramming.com',
    url='http://github.com/danpetrikin/djangoappengine_rdbms',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)
