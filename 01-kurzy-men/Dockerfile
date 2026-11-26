FROM python:3.12-slim
WORKDIR /app
COPY kurzy ./kurzy
ENV HOST=0.0.0.0 PORT=8000 PYTHONUNBUFFERED=1
USER nobody
EXPOSE 8000
CMD ["python", "-m", "kurzy.web"]
