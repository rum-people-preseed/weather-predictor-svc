FROM python:3.10-bullseye

WORKDIR /app
COPY requirements.txt ./
RUN pip3 install --no-cache -r requirements.txt

COPY . ./

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0"]