def validate_mapping(mapping: dict):
    """Ensure mapping JSON is valid and contains required keys."""
    if not isinstance(mapping, dict):
        raise ValueError("Mapping file must be a dictionary.")

    if "renameMapping" not in mapping:
        raise ValueError("Mapping file must contain 'renameMapping' key.")

    if not isinstance(mapping["renameMapping"], dict):
        raise ValueError("'renameMapping' must be a dictionary of field mappings.")

    # Ensure no null or empty keys
    for old, new in mapping["renameMapping"].items():
        if not old or not new:
            raise ValueError("Each mapping must have non-empty old and new field names.")