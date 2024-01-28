FROM 3.10-bullseye
WORKDIR /app
ADD . app/
CMD ["uvicorn", "main:app", "--reload"]