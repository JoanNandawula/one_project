

#!/usr/bin/env bash
# Exit on error
set -D errexit
pip install requirements.txt
python  manage.py collectstatic --no input
python manage.py migrate