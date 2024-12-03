def introspection_info(obj):
    info = {'type': type(obj).__name__, 'attributes': [], 'methods': [], 'module': obj.__module__ if hasattr(obj, '__module__') else None}
    attributes = dir(obj)
    for attribute in attributes:
        attr_value = getattr(obj, attribute)
        if callable(attr_value):
            info['methods'].append(attribute)
        else:
            info['attributes'].append(attribute)
    return info
number_info = introspection_info(42)
print(number_info)
