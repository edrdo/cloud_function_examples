import functions_framework
import google.cloud.storage as gcs
import base64
import os.path
import urllib.parse
import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

def download(url):
  headers = {
    'Api-User-Agent': 'Google Cloud Functions'
  }
  request = urllib.request.Request(url=url, headers=headers)
  return urllib.request.urlopen(request).read()


BUCKET_NAME='bdcc202324'

@functions_framework.cloud_event
def subscribe(event):
    url_to_fetch = base64.b64decode(event.data["message"]["data"]).decode("utf-8")
    print("URL:", url_to_fetch)
    object_name = os.path.basename(urllib.parse.urlparse(url_to_fetch).path)
    data = download(url_to_fetch)
    gcs_client = gcs.Client()
    gcs_bucket = gcs.Bucket(client=gcs_client, name=BUCKET_NAME)
    gcs_blob = gcs.Blob(object_name, bucket=gcs_bucket)
    gcs_blob.upload_from_string(data)
    print("Bucket URI:", gcs_blob.self_link)

