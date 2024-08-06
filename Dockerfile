FROM python:3.10.14-bullseye
EXPOSE 5801
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD streamlit run src/components/app.py --server.port 8080
