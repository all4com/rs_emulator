FROM python:3.11

WORKDIR /work

RUN pip install --upgrade pip

COPY requiriments.txt .
RUN pip install -r requiriments.txt

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]