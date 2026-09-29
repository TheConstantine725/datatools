FROM ghcr.io/astral-sh/uv:python3.13-trixie-slim AS builder

RUN uv pip install --system \
    dagster \
    dagster-graphql \
    dagster-webserver \
    dagster-postgres \
    dagster-docker \
    psycopg[binary] \
    "sqlalchemy<2.1"

# Set $DAGSTER_HOME and copy dagster.yaml and workspace.yaml there
ENV DAGSTER_HOME=/opt/dagster/dagster_home/

RUN mkdir -p $DAGSTER_HOME

COPY ./dagster.yaml ./workspace.yaml $DAGSTER_HOME

WORKDIR $DAGSTER_HOME
