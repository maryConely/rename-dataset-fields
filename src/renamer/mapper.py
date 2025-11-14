def rename_fields(record: dict, mapping: dict) -> dict:
    """Return a new dict with fields renamed according to mapping."""
    if not isinstance(record, dict):
        raise ValueError("Each record must be a dictionary.")
    new_record = {}
    for key, value in record.items():
        new_key = mapping.get(key, key)
        new_record[new_key] = value
    return new_record