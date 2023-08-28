#!/bin/bash

command_output=$(helm status my-flas 2>&1)

expected_error="Error: release: not found"

if [ "$command_output" = "$expected_error" ]; then
    helm install my-flask-app my-flask-app/my-flask-app
else
    helm upgrade --recreate-pods my-flask-app my-flask-app/my-flask-app
fi






