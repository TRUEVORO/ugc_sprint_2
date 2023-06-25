FROM python:3.11.3-slim-buster as build

WORKDIR /opt/ugc

COPY ./requirements.txt .

RUN apt update \
    && python -m venv venv \
    && venv/bin/pip install --no-cache-dir --upgrade pip \
    && venv/bin/pip install --no-cache-dir -r requirements.txt

FROM python:3.11.3-slim-buster

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/opt/ugc/venv/bin:${PATH}"

ARG APP=/opt/ugc
ARG USER=web

WORKDIR ${APP}

RUN apt update \
     && apt install -y --no-install-recommends netcat \
    && rm -rf /var/lib/apt/lists/* \
    && groupadd -r ${USER} \
    && useradd -d ${APP} -r -g ${USER} ${USER}

COPY --chown=${USER}:${USER} --from=build ${APP}/venv ./venv
COPY --chown=${USER}:${USER} . .

RUN chmod +x ${APP}/entrypoint.sh

USER ${USER}

ENTRYPOINT ["/opt/ugc/entrypoint.sh"]
