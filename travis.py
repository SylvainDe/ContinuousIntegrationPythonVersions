import itertools

TRAVIS_CONFIG_FILE = '.travis.yml'
TRAVIS_PYTHON_VERSIONS = [
    'nightly',
    '2.6',
    '2.7',
    '3.2',
    '3.3',
    '3.4',
    '3.5',
    '3.6',
    '3.7',
    '3.8',
    '3.9',
    '3.5-dev',
    '3.6-dev',
    '3.7-dev',
    '3.8-dev',
    '3.9-dev',
    'pypy',
    'pypy2.7-6.0',
    'pypy3',
    'pypy-5.3.1',
    'pypy-5.4.1',
    'pypy3.5-6.0',
]
TRAVIS_DIST = [
    'xenial',  # 16.04
    'trusty',  # 14.04
    'precise',  # 12.04
]
TRAVIS_ALLOWED_FAILURES = [
    ('2.6', 'xenial'),
    ('3.2', 'xenial'),
    ('3.3', 'xenial'),
    ('3.7', 'trusty'),
    ('3.7', 'precise'),
    ('3.8', 'trusty'),
    ('3.8', 'precise'),
    ('3.8-dev', 'trusty'),
    ('3.8-dev', 'precise'),
    ('3.9', 'xenial'),
    ('3.9', 'trusty'),
    ('3.9', 'precise'),
    ('3.9-dev', 'xenial'),
    ('3.9-dev', 'trusty'),
    ('3.9-dev', 'precise'),
    ('pypy-5.3.1', 'xenial'),
    ('pypy-5.4.1', 'xenial'),
    ('pypy2.7-6.0', 'trusty'),
    ('pypy2.7-6.0', 'precise'),
    ('pypy3.5-6.0', 'trusty'),
    ('pypy3.5-6.0', 'precise'),
]


with open(TRAVIS_CONFIG_FILE, 'w') as f:
    f.write("""
language: python

matrix:
  include: """)
    for vers, dist in itertools.product(TRAVIS_PYTHON_VERSIONS, TRAVIS_DIST):
        f.write("""
  - os: linux
    dist: {dist}
    python: {version}""".format(dist=dist, version=vers))
    f.write("""
  allow_failures:""")
    for vers, dist in TRAVIS_ALLOWED_FAILURES:
        f.write("""
  - os: linux
    dist: {dist}
    python: {version}""".format(dist=dist, version=vers))

    f.write("""

script:
 - python -VV
 - python -c "import sys; print(sys._git)" || true
""")
