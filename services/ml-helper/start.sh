#!/bin/bash

set -eux
# Authenticate to the GCP API, setting account credentials as default identity
gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS}
gsutil cp -r ${SRC} ${DEST}
ls -al ${DEST}

