# models/engine/file_storage.py

class FileStorage:
    def __init__(self):
        self.__file_path = "file.json"  # Path to the JSON file
        self.__objects = {}  # Dictionary to store objects by <class name>.id

    def all(self):
        """Returns the dictionary of __objects."""
        return self.__objects

    def new(self, obj):
        """Sets obj in __objects with key <obj class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        serialized_data = {}
        for key, obj in self.__objects.items():
            serialized_data[key] = obj.to_dict()

        with open(self.__file_path, "w") as json_file:
            json.dump(serialized_data, json_file)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(self.__file_path, "r") as json_file:
                data = json.load(json_file)
                for key, value in data.items():
                    class_name, obj_id = key.split(".")
                    obj = globals()class_name
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass  # No existing file, start with an empty __objects

