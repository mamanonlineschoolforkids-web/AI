#!/bin/bash
cd Chatbot
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port $PORT
