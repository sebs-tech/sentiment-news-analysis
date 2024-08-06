FROM python:3.12-slim-bookworm
#COPY . /app
##WORKDIR /app
#RUN pip install -r requirements.txt
#CMD streamlit run src/components/app.py --server.port 8080
WORKDIR /app
COPY requirements.txt src .
RUN pip install -r requirements.txt
CMD streamlit run src/components/app.py --server.port 8080