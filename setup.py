'''
Ark Express
-------
Client library for communicating with of the Ark Express for Delivery Shipping.

Notes
`````
This is still an early release and does not provide access to all the
functionality of the Ark Express API NOAH.  Currently, only submitting
track delivery.

Links
`````
* `Ark Express website <https://track.ark-xpress.com/cp/>`_
'''

from setuptools import setup

pkg_req = [
    'requests==2.3.0',
]


setup(
    name='ArkExpress',
    version=__import__('arkexpress').__version__,
    url='https://github.com/yanwarsolah/arkexpress',
    license='BSD',
    author='Yanwar Solahudin',
    author_email='yanwar@staff.gramedia.com',
    description='Ark Express API Client Library',
    long_description=__doc__,
    packages=['arkexpress',],
    include_package_data=True,
    platforms='any',
    classifiers=['Development Status :: 3 - Alpha',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3.3',
                 'Programming Language :: Python :: 3.4',
                 'Programming Language :: Python :: 3.5',
                 'Programming Language :: Python :: 3.6',
                 ],
    install_requires=pkg_req,
)