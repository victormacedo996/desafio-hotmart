FROM python:3.10.12


WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN apt update && apt upgrade -y 
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
COPY ./main.py /app/
COPY ./src /app/src

EXPOSE 8000


CMD ["python3", "main.py"]