import os

from setuptools import setup, find_packages

setup(
    name='django-social-poster',
    version='0.1',
    description='Signals for posting messages on Facebook and Twitter.',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    author='Raphael Jasjukaitis',
    author_email='webmaster@raphaa.de',
    url='https://github.com/raphaa/django-social-poster',
    license='BSD License',
    platforms=['OS Independent'],
    packages=find_packages(),
    classifiers=[
        'Environment :: Web Environment',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    zip_safe=False,
    include_package_data=True,
    install_requires=['Django',
                      'facepy',
                      'python-twitter'],
)
