from setuptools import setup, find_packages

setup(
    name='django-brokerage',
    version=__import__('brokerage').__version__,
    license="GPLv3",

    install_requires = [
        'django-markup-mixin',
        'django-extensions',
        'simple_history',
        'django-photologue',
        'django-attributes',],

    description='A simple reusable application for managing a real estate brokerage',
    long_description=open('README.rst').read(),

    author='Colin Powell',
    author_email='colin@onecardinal.com',

    url='http://github.com/powellc/django-brokerage',
    download_url='http://github.com/powellc/django-brokerage/downloads',

    include_package_data=True,

    packages=['brokerage'],

    zip_safe=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)
