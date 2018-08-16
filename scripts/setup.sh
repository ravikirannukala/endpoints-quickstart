printf "\n################ Creating Project #####################\n"
gcloud projects create DEMO_PROJECT_ID
printf "\n################ Linking Project To Billing Account and Enabling Billing  #####################\n"
gcloud alpha billing projects link DEMO_PROJECT_ID --billing-account LINKED_ACCT_ID 
gcloud config set project DEMO_PROJECT_ID
printf "\n################ Creating Cloud SQL Instance #####################\n"
gcloud sql instances create developer-api-v1  --authorized-networks=0.0.0.0/0

printf "\n################ Set Root DB User Password  #####################\n"
gcloud sql users set-password root %  --instance developer-api-v1 --password DB_PASSWORD
dbHost=$(gcloud sql instances describe developer-api-v1 --format=json | jq .ipAddresses[0].ipAddress)
sed -i '' -e  's/DB_HOST_NAME/'"${dbHost}"'/g' $(find /tmp/demo -type f)
gcloud sql databases create developers --instance=developer-api-v1
printf "\n################ Creating Cloud Endpoint #####################\n"
gcloud endpoints services deploy ../openapi.yaml
printf  "\n################ Creating GAE Application #####################\n"
gcloud app create --region us-central
gcloud --quiet app deploy  ../app/app.yaml
