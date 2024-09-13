FROM python:3.11

WORKDIR /code

COPY src/samdul00food/main.py /code/

RUN pip install --no-cache-dir --upgrade git+https://github.com/sooj1n/samdul00food-.git@0.1.0

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]
