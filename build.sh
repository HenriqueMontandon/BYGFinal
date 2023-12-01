set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input

python manage.py makemigrations
python manage.py migrate

cat <<EOF | python manage.py shell
import os
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission

User = get_user_model()

if not User.objects.filter(username=os.environ["DJANGO_SUPERUSER_USERNAME"]).exists():
    User.objects.create_superuser(os.environ["DJANGO_SUPERUSER_USERNAME"], os.environ["DJANGO_SUPERUSER_EMAIL"], os.environ["DJANGO_SUPERUSER_PASSWORD"])

empresas_users_group, _ = Group.objects.get_or_create(name="empresas_users")

permissions = ["view_categoria", "view_review"]
permissions_objs = [Permission.objects.get(codename=c) for c in permissions]

for perm in permissions_objs:
    empresas_users_group.permissions.add(perm)

empresas_users_group.save()
EOF