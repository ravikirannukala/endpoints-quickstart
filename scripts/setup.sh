gcloud projects create ravi-test-29-07-2018-2
gcloud config set project ravi-test-29-07-2018-2
gcloud sql instances create INSTANCE developer-api-v1  --authorized-networks=0.0.0.0/0
gcloud sql instances set-root-password developer-api-v1 -p test1234
gcloud endpoints services deploy openapi.yaml