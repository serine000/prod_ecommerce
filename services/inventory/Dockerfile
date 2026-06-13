FROM ghcr.io/astral-sh/uv:trixie-slim AS builder

WORKDIR /app

COPY uv.lock /app

RUN uv init --name src && uv sync ---no-dev --frozen

FROM python:3.13-slim AS runner

COPY src /app/src

COPY --from=builder /app/.venv /app/.venv
ENV PATH="/app/.venv/bin:$PATH"
ENV PYTHONPATH=/app/.venv/lib/python3.13/site-packages

WORKDIR /app

ENTRYPOINT [ "python", "src/main.py"]