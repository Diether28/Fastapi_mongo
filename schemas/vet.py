def vetEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "email": item["email"],
        "password": item["password"]
    }
    
def vetsEntity(entity) -> list:
    return [vetEntity(item) for item in entity]