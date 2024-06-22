import os
import json

# Define the base URL for your API
base_url = 'http://127.0.0.1:5000'

# Get the list of models by inspecting the models directory
models_dir = 'models'
entities = {}
for filename in os.listdir(models_dir):
    if filename.endswith('.py') and filename != '__init__.py':
        entity_name = filename[:-3].capitalize() + 's'
        entities[entity_name] = [
            {'name': f'Get All {entity_name}', 'method': 'GET', 'endpoint': f'/{entity_name.lower()}/'},
            {'name': f'Get {entity_name[:-1]} by ID', 'method': 'GET', 'endpoint': f'/{entity_name.lower()}/:id'},
            {'name': f'Create {entity_name[:-1]}', 'method': 'POST', 'endpoint': f'/{entity_name.lower()}/', 'body': '{}'},
            {'name': f'Update {entity_name[:-1]}', 'method': 'PUT', 'endpoint': f'/{entity_name.lower()}/:id', 'body': '{}'},
            {'name': f'Delete {entity_name[:-1]}', 'method': 'DELETE', 'endpoint': f'/{entity_name.lower()}/:id'}
        ]

# Create the Postman collection JSON structure
collection = {
    "info": {
        "name": "Cat Foster Community API",
        "description": "Postman collection for the Cat Foster Community API",
        "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
    },
    "item": []
}

# Add items to the collection
for entity, endpoints in entities.items():
    folder = {
        "name": entity,
        "item": []
    }
    for endpoint in endpoints:
        item = {
            "name": endpoint['name'],
            "request": {
                "method": endpoint['method'],
                "header": [
                    {
                        "key": "Content-Type",
                        "value": "application/json"
                    }
                ],
                "url": {
                    "raw": base_url + endpoint['endpoint'],
                    "protocol": "http",
                    "host": ["127", "0", "0", "1"],
                    "port": "5000",
                    "path": endpoint['endpoint'].strip('/').split('/')
                }
            }
        }
        if 'body' in endpoint:
            item['request']['body'] = {
                "mode": "raw",
                "raw": endpoint['body']
            }
        folder['item'].append(item)
    collection['item'].append(folder)

# Save the collection to a JSON file in tht utils directory
with open('utils/cat_foster_community_api.postman_collection.json', 'w') as f:
    json.dump(collection, f, indent=4)

print("Postman collection generated successfully")
