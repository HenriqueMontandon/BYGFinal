set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
# adicione linhas abaixo
python manage.py migrate

# create superuser if missing
cat <<EOF | python manage.py shell
import os
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission

User = get_user_model()

User.objects.filter(username=os.environ["DJANGO_SUPERUSER_USERNAME"]).exists() or \
    User.objects.create_superuser(os.environ["DJANGO_SUPERUSER_USERNAME"], os.environ["DJANGO_SUPERUSER_EMAIL"], os.environ["DJANGO_SUPERUSER_PASSWORD"])

g = Group(name="empresas_users")
g.permissions.set([Permission.objects.get(codename=c) for c in ["view_categoria", "view_review", "view_categorie", "view_comment"]])
Group.objects.filter(name="empresas_users").exists() or g.save()
EOF