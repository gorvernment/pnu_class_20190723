import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hellodj.settings')
import django
django.setup()

from django.core.serializers.json import DjangoJSONEncoder
from pokemon.models import Pokemon

pokemon = Pokemon.objects.all().first()

print(pokemon)

class MyEncoder(DjangoJSONEncoder):
    def default(self, o):
        if isinstance(o, Pokemon):
            return {
                'name': o.name,
                'page_url': o.page_url,
            }
        return super().default(o)

import json
json_string = json.dumps(pokemon, cls=MyEncoder)
print(json_string)