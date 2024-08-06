FROM python:3.12-slim-bookworm
WORKDIR /app
COPY requirements.txt .
COPY src/ ./src
COPY nlp  ./nlp
RUN pip install -r requirements.txt
CMD streamlit run src/components/app.py --server.port 8080