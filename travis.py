import itertools

TRAVIS_CONFIG_FILE = '.travis.yml'
TRAVIS_PYTHON_VERSIONS = [
    'nightly',
    '2.6',
    '2.7',
    '3.0',
    '3.1',
    '3.2',
    '3.3',
    '3.4',
    '3.5',
    '3.6',
    '3.7',
    '3.8',
    '2.6-dev',
    '2.7-dev',
    '3.0-dev',
    '3.1-dev',
    '3.2-dev',
    '3.3-dev',
    '3.4-dev',
    '3.5-dev',
    '3.6-dev',
    '3.7-dev',
    '3.8-dev',
    'pypy',
    'pypy3',
    'pypy-5.3.1',
    'pypy-5.4.1',
]
TRAVIS_DIST = ['xenial', 'trusty', 'precise']

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

script:
 - python -VV
 - python -c "import sys; print(sys._git)" || true
""")
