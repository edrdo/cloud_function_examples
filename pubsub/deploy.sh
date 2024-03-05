gcloud functions deploy process_url_function \
  --gen2 --runtime=python312 --region=us-central1 \
  --source=. --entry-point=subscribe --trigger-topic=PROCESS_URL \
  --allow-unauthenticated

