FROM python:3.9

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

RUN --mount=type=secret,id=AIWHO_API_KEY \
    echo 'AIWHO_APP_NAME="AI Who Is"' > /app/.env && \
    echo 'AIWHO_DEBUG=false' >> /app/.env && \
    echo 'AIWHO_API_HOST=0.0.0.0' >> /app/.env && \
    echo 'AIWHO_API_PORT=8000' >> /app/.env && \
    echo "AIWHO_API_KEY=$(cat /run/secrets/AIWHO_API_KEY)" >> /app/.env

COPY src/ /app/src
COPY data/ /app/data

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]