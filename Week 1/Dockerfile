FROM python:3.9

RUN pip install pandas

WORKDIR /app
COPY ny_taxi.ipynb ny_taxi.ipynb

ENTRYPOINT [ "python", "ny_taxi.ipynb" ]