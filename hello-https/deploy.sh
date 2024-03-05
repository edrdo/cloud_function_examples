gcloud functions deploy hello-function \
  --gen2 --runtime=python312 --region=us-central1 \
  --source=. --entry-point=hello_via_http --trigger-http \
  --allow-unauthenticated