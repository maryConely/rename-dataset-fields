import json
import os
from renamer.mapper import rename_fields
from renamer.validator import validate_mapping
from utils.io_handler import load_json, save_json

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_dir, "config", "mapping.example.json")
    input_path = os.path.join(os.path.dirname(base_dir), "data", "input.sample.json")
    output_path = os.path.join(os.path.dirname(base_dir), "data", "output.sample.json")

    mapping = load_json(config_path)
    validate_mapping(mapping)

    dataset = load_json(input_path)
    if not isinstance(dataset, list):
        raise ValueError("Input dataset must be a list of objects.")

    renamed = [rename_fields(item, mapping["renameMapping"]) for item in dataset]
    save_json(output_path, renamed)

    print(f"Renaming complete. Output written to {output_path}")

if __name__ == "__main__":
    main()