FROM python:3.11.4-slim-bullseye as stage-build
ARG TARGETARCH

ARG VERSION
ENV VERSION=$VERSION

WORKDIR /opt/fortserver
ADD . .
RUN cd utils && bash -ixeu build.sh

FROM python:3.11.4-slim-bullseye
ARG TARGETARCH
MAINTAINER fortserver Team <ibuler@qq.com>

ARG BUILD_DEPENDENCIES="              \
        g++                           \
        make                          \
        pkg-config"

ARG DEPENDENCIES="                    \
        freetds-dev                   \
        libpq-dev                     \
        libffi-dev                    \
        libjpeg-dev                   \
        libldap2-dev                  \
        libsasl2-dev                  \
        libssl-dev                    \
        libxml2-dev                   \
        libxmlsec1-dev                \
        libxmlsec1-openssl            \
        freerdp2-dev                  \
        libaio-dev"

ARG TOOLS="                           \
        ca-certificates               \
        curl                          \
        default-libmysqlclient-dev    \
        default-mysql-client          \
        locales                       \
        openssh-client                \
        procps                        \
        sshpass                       \
        telnet                        \
        unzip                         \
        vim                           \
        git                           \
        nmap                          \
        wget"

ARG APT_MIRROR=http://mirrors.ustc.edu.cn

RUN --mount=type=cache,target=/var/cache/apt,sharing=locked,id=core \
    sed -i "s@http://.*.debian.org@${APT_MIRROR}@g" /etc/apt/sources.list \
    && rm -f /etc/apt/apt.conf.d/docker-clean \
    && ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && apt-get update \
    && apt-get -y install --no-install-recommends ${BUILD_DEPENDENCIES} \
    && apt-get -y install --no-install-recommends ${DEPENDENCIES} \
    && apt-get -y install --no-install-recommends ${TOOLS} \
    && mkdir -p /root/.ssh/ \
    && echo "Host *\n\tStrictHostKeyChecking no\n\tUserKnownHostsFile /dev/null\n\tCiphers +aes128-cbc\n\tKexAlgorithms +diffie-hellman-group1-sha1\n\tHostKeyAlgorithms +ssh-rsa" > /root/.ssh/config \
    && echo "set mouse-=a" > ~/.vimrc \
    && echo "no" | dpkg-reconfigure dash \
    && echo "zh_CN.UTF-8" | dpkg-reconfigure locales \
    && sed -i "s@# export @export @g" ~/.bashrc \
    && sed -i "s@# alias @alias @g" ~/.bashrc \
    && rm -rf /var/lib/apt/lists/*

ARG DOWNLOAD_URL=https://download.fortserver.org

RUN set -ex \
    && \
    if [ "${TARGETARCH}" == "amd64" ] || [ "${TARGETARCH}" == "arm64" ]; then \
        mkdir -p /opt/oracle; \
        cd /opt/oracle; \
        wget ${DOWNLOAD_URL}/public/instantclient-basiclite-linux.${TARGETARCH}-19.10.0.0.0.zip; \
        unzip instantclient-basiclite-linux.${TARGETARCH}-19.10.0.0.0.zip; \
        echo "/opt/oracle/instantclient_19_10" > /etc/ld.so.conf.d/oracle-instantclient.conf; \
        ldconfig; \
        rm -f instantclient-basiclite-linux.${TARGETARCH}-19.10.0.0.0.zip; \
    fi

WORKDIR /tmp/build
COPY ./pyproject.toml ./pyproject.toml
COPY ./poetry.lock ./poetry.lock

ARG PIP_MIRROR=https://pypi.douban.com/simple

RUN --mount=type=cache,target=/root/.cache/pip \
    set -ex \
    && pip install poetry==1.5.1 -i ${PIP_MIRROR} \
    && poetry install --only=main

COPY --from=stage-build /opt/fortserver/release/fortserver /opt/fortserver
RUN echo > /opt/fortserver/config.yml \
    && rm -rf /tmp/build

WORKDIR /opt/fortserver
VOLUME /opt/fortserver/data
VOLUME /opt/fortserver/logs

ENV LANG=zh_CN.UTF-8

EXPOSE 8080

ENTRYPOINT ["./entrypoint.sh"]
