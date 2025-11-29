from oev.translate import ArchaicEnglish
import import_toml
import json

# Load config once and cache it
config = import_toml.load_toml_from_parent("config.toml")
oev_config = config.get('oev', {})
print(oev_config)

chaos = oev_config.get('chaos', 0.35)
replace_chance = oev_config.get('replace_chance', 0.5)
print(chaos,replace_chance)
translator = ArchaicEnglish(chaos=chaos, replace_chance=replace_chance)

def translate_verses(obj):
    """
    Recursively traverse the JSON and translate only 'text' fields.
    """
    if isinstance(obj, dict):
        new_obj = {}
        for k, v in obj.items():
            if k == "text" and isinstance(v, str):
                new_obj[k] = translator.translate(v)  # translate only verse text
            else:
                new_obj[k] = translate_verses(v)
        return new_obj
    elif isinstance(obj, list):
        return [translate_verses(item) for item in obj]
    else:
        return obj  # numbers, None, etc. stay unchanged

# Load the KJV JSON
with open('kjv.min.json','r') as f:
    kjv = json.load(f)

# Translate only verse texts
gzv = translate_verses(kjv)

# Write the output safely
with open('oev.min.json','w') as f:
    json.dump(gzv, f, indent=2)
