#!/usr/bin/env python

from setuptools import *

setup(
	name='mocktest',
	version='0.5.1',
	description='a mocking and expectation test library for python, inspired by rspec',
	author='Tim Cuthbertson',
	author_email='tim3d.junk+mocktest@gmail.com',
	url='http://gfxmonk.net/dist/0install/mocktest.xml',
	
	long_description="""\
	mocktest is a mocking and expectation test library for python.
	It is similar to rspec's should_receive and associated matchers, and
	offers a compatible unittest TestCase base class for automatically
	verifying expectations.
	""",
	classifiers=[
		"License :: OSI Approved :: BSD License",
		"Programming Language :: Python",
		"Development Status :: 4 - Beta",
		"Intended Audience :: Developers",
		"Topic :: Software Development :: Libraries :: Python Modules",
		"Topic :: Software Development :: Testing",
	],
	keywords='test mock expect expectation stub rspec unittest',
	license='GPLv3',
	install_requires=[
		'setuptools',
	],
	packages=['mocktest', 'mocktest.matchers', 'mocktest.lib'],
)
