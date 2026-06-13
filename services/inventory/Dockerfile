FROM python:3.13-slim

WORKDIR /app

COPY --from=ghcr.io/astral-sh/uv:0.9.2 /uv /bin/

COPY uv.lock /app

RUN uv init --name src && uv sync --frozen

COPY src /app/src

ENTRYPOINT [ "uv", "run", "python", "src/main.py"]