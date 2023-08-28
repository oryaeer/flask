#!/bin/bash
# Navigate to the chart directory
cd /home/oryaeer/Desktop/flask/bitcoinproject/my-first-flask/
# Extract the current version from Chart.yaml
VERSION=$(grep "version:" Chart.yaml | cut -d ' ' -f 2)
# Split the version into major, minor, and patch numbers
MAJOR=$(echo $VERSION | cut -d '.' -f 1)
MINOR=$(echo $VERSION | cut -d '.' -f 2)
PATCH=$(echo $VERSION | cut -d '.' -f 3)
# Increment the patch number
PATCH=$((PATCH + 1))
# Construct the new version number
NEW_VERSION="$MAJOR.$MINOR.$PATCH"
# Update Chart.yaml with the new version
sed -i "s/version: $VERSION/version: $NEW_VERSION/g" /home/oryaeer/Desktop/flask/bitcoinproject/my-first-flask/Chart.yaml
# Package the helm chart
helm package . --destination /tmp --version $NEW_VERSION --app-version $NEW_VERSION
helm repo index . --destination /tmp
# Rename the package
mv /tmp/my-flask-app-$NEW_VERSION.tgz /tmp/my-flask-app-$NEW_VERSION.tgz
# Push the package to the GCP bucket
gsutil cp /tmp/my-flask-app-$NEW_VERSION.tgz gs://helmoryaeer
gsutil cp /tmp/index.yaml gs://helmoryaeer
# Cleanup
rm /tmp/my-flask-app-$NEW_VERSION.tgz
echo "Chart helm-project-$NEW_VERSION.tgz has been uploaded to the bucket-helmoryaeer."
# List all versions, sorted
ALL_VERSIONS=$(gsutil ls gs://helmoryaeer | grep my-flask-app | sort)
# Count total versions
COUNT=$(echo "$ALL_VERSIONS" | wc -l)
# Calculate how many to delete
DELETE_COUNT=$((COUNT - 5))
# Loop and delete oldest versions if there are more than 5
if [ $DELETE_COUNT -gt 0 ]; then
    echo "$ALL_VERSIONS" | head -n $DELETE_COUNT | while read -r version; do
        gsutil rm "$version"
        echo "Deleted old version: $version"
    done
fi