FROM ghcr.io/astral-sh/uv:python3.11-trixie-slim AS builder

ENV UV_COMPILE_BYTECODE=1\
    UV_LINK_MODE=copy\
    PYTHONBUFFERED=1

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync  --frozen --no-install-project --no-dev

COPY . .
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-install-project --no-dev

FROM python:3.11-slim-bookworm AS runtime

WORKDIR /app

COPY --from=builder /app /app

ENV PATH="/app/.venv/bin:$PATH"\
    PYTHONBUFFERED=1\
    DAGSTER_HOME=/opt/dagster/home

RUN mkdir -p $DAGSTER_HOME

EXPOSE 4000

CMD ["dagster", "api", "grpc", "-h", "0.0.0.0", "-p", "4000", "-m", "datatools.definitions"]
