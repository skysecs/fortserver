FROM fortserver/core-base:20240919_024156 AS stage-build

ARG VERSION

WORKDIR /opt/fortserver

ADD . .

RUN echo > /opt/fortserver/config.yml \
    && \
    if [ -n "${VERSION}" ]; then \
        sed -i "s@VERSION = .*@VERSION = '${VERSION}'@g" apps/fortserver/const.py; \
    fi

RUN set -ex \
    && export SECRET_KEY=$(head -c100 < /dev/urandom | base64 | tr -dc A-Za-z0-9 | head -c 48) \
    && . /opt/py3/bin/activate \
    && cd apps \
    && python manage.py compilemessages


FROM python:3.11-slim-bullseye
ENV LANG=en_US.UTF-8 \
    PATH=/opt/py3/bin:$PATH

ARG DEPENDENCIES="                    \
        libldap2-dev                  \
        libx11-dev"

ARG TOOLS="                           \
        ca-certificates               \
        default-libmysqlclient-dev    \
        openssh-client                \
        sshpass                       \
        bubblewrap"

ARG APT_MIRROR=http://deb.debian.org
RUN set -ex \
    && rm -f /etc/apt/apt.conf.d/docker-clean \
    && sed -i "s@http://.*.debian.org@${APT_MIRROR}@g" /etc/apt/sources.list \
    && ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && apt-get update > /dev/null \
    && apt-get -y install --no-install-recommends ${DEPENDENCIES} \
    && apt-get -y install --no-install-recommends ${TOOLS} \
    && apt-get clean \
    && mkdir -p /root/.ssh/ \
    && echo "Host *\n\tStrictHostKeyChecking no\n\tUserKnownHostsFile /dev/null\n\tCiphers +aes128-cbc\n\tKexAlgorithms +diffie-hellman-group1-sha1\n\tHostKeyAlgorithms +ssh-rsa" > /root/.ssh/config \
    && echo "no" | dpkg-reconfigure dash \
    && sed -i "s@# export @export @g" ~/.bashrc \
    && sed -i "s@# alias @alias @g" ~/.bashrc

COPY --from=stage-build /opt /opt
COPY --from=stage-build /usr/local/bin /usr/local/bin
COPY --from=stage-build /opt/fortserver/apps/libs/ansible/ansible.cfg /etc/ansible/

WORKDIR /opt/fortserver

VOLUME /opt/fortserver/data

ENTRYPOINT ["./entrypoint.sh"]

EXPOSE 8080

STOPSIGNAL SIGQUIT

CMD ["start", "all"]
