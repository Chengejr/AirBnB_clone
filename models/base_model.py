
import uuid
from datetime import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        """
        Initializes a BaseModel instance.
        """
        if kwargs:
            # If kwargs is not empty, set instance attributes from the dictionary
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
                    if key in ('created_at', 'updated_at'):
                        # Convert string datetime to datetime object
                        setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
        else:
            # Otherwise, create new instance with id and created_at
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the public instance attribute 'updated_at' with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of the instance.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

# Example usage
if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My First Model"
    my_model.my_number = 89
    print(my_model)

    my_model.save()
    print(my_model)

    my_model_json = my_model.to_dict()
    print(my_model_json)

    print("JSON of my_model:")
    for key, value in my_model_json.items():
        print(f"\t{key}: ({type(value).__name__}) - {value}")

    print("--")
    my_new_model = BaseModel(**my_model_json)
    print(my_new_model.id)
    print(my_new_model)
    print(type(my_new_model.created_at))

    print("--")
    print(my_model is my_new_model)
