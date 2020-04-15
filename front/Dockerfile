FROM python:3.6-alpine as base

FROM base as builder
WORKDIR /install
COPY app/requirements.txt .
RUN pip install --install-option="--prefix=/install" -r requirements.txt

FROM base
COPY --from=builder /install /usr/local
WORKDIR /app
COPY /app .

CMD ["python3", "app.py"]