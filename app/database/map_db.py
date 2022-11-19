from .base import Base


class MapDB(Base):

    db = 'app/database/map.json'
    
    def get_map_info(self, json_name: str = db) -> dict:

        db = self.read_json_db(json_name)
        
        tags = list(db.keys())
        names = list(item['name'] for item in db.values())
        pos = list(item['pos'] for item in db.values())

        return {
            'tag': tags,
            'name': names,
            'pos': pos,
        }