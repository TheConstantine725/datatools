FROM ghcr.io/astral-sh/uv:python3.13-trixie-slim AS builder

ENV UV_COMPILE_BYTECODE=1\
    UV_LINK_MODE=copy\
    PYTHONBUFFERED=1

WORKDIR /app

COPY . .

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync  --frozen --no-dev

ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 4000

HEALTHCHECK --timeout=1s --start-period=3s --interval=3s --retries=20 CMD ["uv", "run", "dagster", "api", "grpc-health-check", "-p", "4000"]

CMD ["uv", "run", "dagster", "code-server", "start", "-h", "0.0.0.0", "-p", "4000", "-m", "datatools.definitions"]
