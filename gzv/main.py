from gzv.translate import to_genz
import json

def translate_verses(obj):
    """
    Recursively traverse the JSON and translate only 'text' fields.
    """
    if isinstance(obj, dict):
        new_obj = {}
        for k, v in obj.items():
            if k == "text" and isinstance(v, str):
                new_obj[k] = to_genz(v)  # translate only verse text
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
with open('gzv.min.json','w') as f:
    json.dump(gzv, f, indent=2)
