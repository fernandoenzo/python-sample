# encoding:utf-8

# Enlace con la documentación completa sobre cómo configurar este archivo: https://packaging.python.org/tutorials/packaging-projects/

from autopackage.parsers.setup_parser import SetupParser
from setuptools import find_packages

name = 'sample'

version = '1.0.0'

description = 'Proyecto Sample'

long_description = "Proyecto Sample"

author = 'Fernando Enzo Guarini'
author_email = 'fernandoenzo@gmail.com'

url = 'https://linuxdevtips.blogspot.com/'
download_url = 'https://github.com/fernandoenzo/sample/'

packages = find_packages()

licencia = 'GPLv3+'

zip_safe = False

keywords = 'sample template django project star wars'

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Console',
    'Intended Audience :: End Users/Desktop',
    'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
    'Natural Language :: Spanish',
    'Operating System :: POSIX :: Linux',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Topic :: System :: Installation/Setup',
]

entry_points = {
    'console_scripts': [
        'bin1 = sample.bin.bin1:sumado',
        'bin2 = sample.bin.bin2:muestra_foto',
    ]
}

package_data = {
    'sample': [
        'static/*'
    ],
}

SetupParser(name=name, version=version, packages=packages, description=description, long_description=long_description, author=author, author_email=author_email, url=url, download_url=download_url,
            license=licencia, keywords=keywords, classifiers=classifiers, entry_points=entry_points, zip_safe=zip_safe, package_data=package_data)
