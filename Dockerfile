FROM python:3.10-slim

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . /app

EXPOSE 8000

ENV LANGCHAIN_TRACING_V2=true
ENV LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
ENV LANGCHAIN_PROJECT="enigma_module"

CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]

