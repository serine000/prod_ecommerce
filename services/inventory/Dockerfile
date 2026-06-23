FROM ghcr.io/astral-sh/uv:0.11.21-python3.13-trixie AS builder

# Omit development dependencies
ENV UV_NO_DEV=1

ENV UV_COMPILE_BYTECOE=1
ENV UV_LINK_MODE=copy

# don't download your own python, use the system one
ENV UV_PYTHON_DOWNLOADS=0 


WORKDIR /app

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-dev

ADD . /app

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev

# Using the python runtime image - tied to docker image
FROM python:3.13-slim-trixie

RUN groupadd --system gid 999 nonroot \
    && useradd --system --gid 999 --uid 99 --create-home nonroot

# We're just copying the app into the runtime image (no uv-installed python runtime)
COPY --from=builder --chown=nonroot:nonroot /app /app

# Place executables in the environment at the front of the path
ENV PATH="/app/.venv/bin:$PATH"

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

# Use the non-root user to run our application
USER nonroot

# Use `/app` as the working directory
WORKDIR /app

ENTRYPOINT ["python", "src/main.py"]