"""
Enclose property names in double quotes in order to JSON serialize the contents in the API
"""
CUSTOMIZATIONS = {
    "serializers": {"Address": {"includeFields": ["id", "city", "province"]}}
}
