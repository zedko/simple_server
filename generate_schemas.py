from models import MODELS_WITH_SCHEMAS
from settings import SCHEMAS_FILES_PATH

if __name__ == '__main__':
    for model in MODELS_WITH_SCHEMAS:
        SCHEMAS_FILES_PATH.mkdir(parents=True, exist_ok=True)
        file_name = SCHEMAS_FILES_PATH / f'{model.__name__}.schema.json'

        with open(file_name, mode='w', encoding='UTF-8') as file:
            print(f'creating scheme for {model.__name__} in {file_name}')
            file.write(model.schema_json(indent=2))
