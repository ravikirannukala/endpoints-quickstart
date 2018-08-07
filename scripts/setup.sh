gcloud projects create DEMO_PROJECT_ID
gcloud alpha billing projects link DEMO_PROJECT_ID --billing-account LINKED_ACCT_ID 
gcloud config set project DEMO_PROJECT_ID
gcloud sql instances create developer-api-v1  --authorized-networks=0.0.0.0/0
gcloud sql users set-password root %  --instance developer-api-v1 --password DB_PASSWORD
dbHost=$(gcloud sql instances describe developer-api-v1 --format=json | jq .ipAddresses[0].ipAddress)
sed -i '' -e  's/DB_HOST_NAME/'"${dbHost}"'/g' $(find /tmp/demo -type f)
gcloud sql databases create developers --instance=developer-api-v1
gcloud endpoints services deploy ../openapi.yaml
gcloud app create --region us-central
gcloud --quiet app deploy  ../app/app.yaml
