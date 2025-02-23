FROM python:3.9
WORKDIR /app
COPY loadtest_fastapi/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .