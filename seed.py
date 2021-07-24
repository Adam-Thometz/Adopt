"""Seed file"""

from models import Pet, db
from app import app

db.drop_all()
db.create_all()

fred = Pet(name="Fred", species="porcupine", photo_url="https://cdn.britannica.com/16/93516-050-3FB4ABE4/Cape-porcupine.jpg", age=5, notes="He knows how to use a camera, be careful")
oliver = Pet(name="Oliver", species="cat", photo_url="https://i.guim.co.uk/img/media/26392d05302e02f7bf4eb143bb84c8097d09144b/446_167_3683_2210/master/3683.jpg?width=620&quality=45&auto=format&fit=max&dpr=2&s=6fe0ebd22151102996062fa1287f824c")
zeus = Pet(name="Zeus", species="dog", age=12, notes="Camera shy but gorgeous!", is_available=False)

db.session.add_all([fred, oliver, zeus])

db.session.commit()