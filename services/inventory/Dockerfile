FROM ghcr.io/astral-sh/uv:0.11.21-python3.13-trixie AS builder

ENV UV_COMPILE_BYTECOE=1
ENV UV_LINK_MODE=copy

ENV UV_PYTHON_DOWNLOADS=0 
# don't download your own python, use the system one


WORKDIR /app

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-dev

ADD . /app

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev

FROM python:3.13-slim-trixie

COPY --from=builder --chown=app:app /app /app

ENV PATH="/app/.venv/bin:$PATH"

ENTRYPOINT ["python", "src/main.py"]