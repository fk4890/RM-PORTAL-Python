FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1
WORKDIR /app

# Minimal system dependencies (build tools + MySQL client headers)
RUN apt-get update \
  && apt-get install -y --no-install-recommends build-essential default-libmysqlclient-dev pkg-config \
  && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip setuptools wheel \
  && pip install --no-cache-dir -r requirements.txt

COPY . .

# Default command (compose overrides this)
# Django プロジェクト名を config にリネームしたのでエントリポイントを修正
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
