FROM python:3-alpine
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r ./requirements.txt
WORKDIR src/
COPY ./src .
CMD ["python", "main.py"]
