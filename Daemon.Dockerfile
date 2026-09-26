# syntax=docker/dockerfile:1

FROM ghcr.io/astral-sh/uv:python3.11-bookworm-slim AS base

ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    PYTHONUNBUFFERED=1

WORKDIR /opt/dagster/app

RUN uv pip install --system --no-cache \
    dagster \
    dagster-postgres \
    dagster-docker

COPY workspace.yaml /opt/dagster/app/workspace.yaml

ENV DAGSTER_HOME=/opt/dagster/dagster_home
RUN mkdir -p $DAGSTER_HOME
COPY dagster.yaml $DAGSTER_HOME/dagster.yaml

ENTRYPOINT ["dagster-daemon", "run"]
