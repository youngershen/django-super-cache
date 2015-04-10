from setuptools import setup, find_packages

version = '0.1a1'

setup(name='django-super-cache',
      version=version,
      description="a page cache plugin, enable you to cache your single page to file or redis.",
      long_description="""\
      a page cache plugin, enable you to cache your single page to file or redis
      """,
      classifiers=['Development Status :: 2 - Pre-Alpha',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Natural Language :: English',
                   'Programming Language :: Python :: 2.7',
                   ],
      keywords='django-super-cache, django, cache, page, page cache',
      author='younger shen',
      author_email='younger.x.shen@gmail.com',
      url='https://github.com/youngershen/django-super-cache',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
          'Django >= 1.6',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
