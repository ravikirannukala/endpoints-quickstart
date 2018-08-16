rm -rf /tmp/demo
cp -r ../. /tmp/demo
sed -i '' -e  's/DEMO_PROJECT_ID/'"${1}"'/g' $(find /tmp/demo -type f)
sed -i '' -e 's/DB_PASSWORD/'"${2}"'/g' $(find /tmp/demo  -type f)
sed -i '' -e 's/LINKED_ACCT_ID/'"${3}"'/g' $(find /tmp/demo -type f)
cd /tmp/demo/scripts
./setup.sh
