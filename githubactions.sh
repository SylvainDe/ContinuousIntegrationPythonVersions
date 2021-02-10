wget https://raw.githubusercontent.com/actions/python-versions/main/versions-manifest.json
sed -n 's/.*"version": "\(.*\)",.*/\1/gp' versions-manifest.json

wget https://downloads.python.org/pypy/versions.json
sed -n 's/.*"pypy_version": "\(.*\)",.*/\1/gp' versions.json
