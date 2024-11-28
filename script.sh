#!/bin/bash

# Build the Docker image
docker build -t hello-world-python .

# Scan the image with Trivy
trivy image hello-world-python

# If vulnerabilities are found, exit with a non-zero status
if [ $? -ne 0 ]; then
  echo "Vulnerabilities found. Build failed."
  exit 1
fi