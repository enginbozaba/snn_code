from setuptools import setup
import os

setup(
    name='snn_code',
    version='0.1.%s' % os.environ.get('TRAVIS_BUILD_NUMBER', 0),
    description='Snn desing',
    author='Me',
    author_email='info@python-private-package-index.com',
    license='MIT',
    packages=['code'],
    url='https://github.com/enginbozaba/snn_code',
    zip_safe=False
)
