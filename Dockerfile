FROM python:3.8-slim-buster AS builder
ADD . /app
WORKDIR /app

RUN pip3 install --target=/app -r requirements.txt

FROM gcr.io/distroless/python3-debian10
COPY --from=builder /app /app
WORKDIR /app
ENV PYTHONPATH /app
CMD ["/app/main.py"]
