
import uvicorn
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel

# ✅ Database configurations
# SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"  # SQLite database
engine = create_engine("postgresql://postgres:ashish@localhost:5432/Demo")

# ✅ Creating session and base class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# ✅ SQLAlchemy model for 'items' table
class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)

# ✅ Create database tables
Base.metadata.create_all(bind=engine)

# ✅ Initialize FastAPI app
app = FastAPI()

# ✅ Pydantic model for request validation
class ItemCreate(BaseModel):
    name: str
    description: str

# ✅ Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ✅ Create (POST)
@app.post("/items/")
async def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    db_item = Item(name=item.name, description=item.description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return {"id":db_item.id}

# ✅ Read (GET)
@app.get("/items/{item_id}")
async def read_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

# ✅ Update (PUT)
@app.patch("/items/{item_id}")
async def update_item(item_id: int, item: ItemCreate, db: Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    db_item.name = item.name
    db_item.description = item.description
    db.commit()
    db.refresh(db_item)
    return db_item

# ✅ Delete (DELETE)
@app.delete("/items/{item_id}")
async def delete_item(item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_item)
    db.commit()
    return {"message": "Item deleted successfully"}

# ✅ Run the FastAPI application
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8001)

