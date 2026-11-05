FROM python:3.12-slim
WORKDIR /app
COPY demo-app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY demo-app/app.py .
EXPOSE 5000
HEALTHCHECK --interval=2s --timeout=2s --retries=15 CMD python -c "import urllib.request as u; u.urlopen('http://localhost:5000/api/health')"
CMD ["python", "app.py"]
