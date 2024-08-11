# Define variables for backend and frontend directories
BACKEND_DIR = backend
FRONTEND_DIR = frontend

start-backend:
	cd $(BACKEND_DIR) && pip3 install -r requirements.txt && uvicorn app.main:app --host 0.0.0.0 --port 8000

start-frontend:
	cd $(FRONTEND_DIR) && pip3 install -r requirements.txt && streamlit run app.py

up:
	$(MAKE) start-backend &
	$(MAKE) start-frontend
