#!/bin/bash
#
# 该build基于registry.fortserver.com/public/python:3
utils_dir=$(pwd)
project_dir=$(dirname "$utils_dir")
release_dir=${project_dir}/release

# 打包
cd "${project_dir}" || exit 3
rm -rf "${release_dir:?}"/*
to_dir="${release_dir}/fortserver"
mkdir -p "${to_dir}"

if [[ -d '.git' ]];then
  command -v git || yum -y install git
  git archive --format tar HEAD | tar x -C "${to_dir}"
else
  cp -R . /tmp/fortserver
  mv /tmp/fortserver/* "${to_dir}"
fi

if [[ $(uname) == 'Darwin' ]];then
  alias sedi="sed -i ''"
else
  alias sedi='sed -i'
fi

# 修改版本号文件
if [[ -n ${VERSION} ]]; then
  sedi "s@VERSION = .*@VERSION = \"${VERSION}\"@g" "${to_dir}/apps/fortserver/const.py"
fi

