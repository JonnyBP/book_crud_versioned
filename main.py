from fastapi import FastAPI
from config.config_variables import settings
from fastapi import FastAPI
from routes.v1_routes import router as v1_router
from routes.v2_routes import router as v2_router
from database.database import Base, engine, init_db

# Crea tablas
Base.metadata.create_all(bind=engine)

# Inserta datos iniciales si no existen
init_db()

app = FastAPI(title="Book API Versioned")

app.include_router(v1_router, prefix="/api/v1")
app.include_router(v2_router, prefix="/api/v2")