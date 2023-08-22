#!/bin/bash

command_output=$(helm status my-gcs-repo 2>&1)

expected_error="Error: release: not found"

if [ "$command_output" = "$expected_error" ]; then
    helm install my-gcs-repo /var/lib/jenkins/workspace/Helm_Pipeline/bitcoinproject/my-first-flask
else
    helm upgrade --recreate-pods my-gcs-repo /var/lib/jenkins/workspace/Helm_Pipeline/bitcoinproject/my-first-flask
fi






