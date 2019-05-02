# YandexVision using experience
# only free options (Images classificayion & Face detection)
# read more https://cloud.yandex.ru/services/vision

import base64
import json
import os
import subprocess

# modified recommended function  https://cloud.yandex.ru/docs/vision/operations/face-detection/ (in Python)
def encode_file(file):
    with open(file, 'rb') as f:
        file_content = f.read()
    return base64.b64encode(file_content).decode('utf-8')

outfile = encode_file('pic1.jpg') #my image file 

out = {
    "folderId": "b1gvtq66beduinpp6mmp",
    "analyze_specs": [{
        "content": outfile,
        "features": [{
            "type": "CLASSIFICATION",
            "classificationConfig": {
                "model": "quality"
            }
},
        {
            "type": "CLASSIFICATION",
            "classificationConfig": {
                "model": "moderation"
            }
        },
            {
            "type": "FACE_DETECTION"
        }]
    }]
}
    
#make request
with open('body.json', 'w') as f:
    json.dump(out, f)
    
# Make command strings  
cloud_id = {"yandexPassportOauthToken": "AQAAAAAJ60K5AATuwezqKbMOR0T2kKrR-ovdNd8"}
get_token = ''.join(("curl -X POST -H 'Content-Type: application/json' -d \"", str(cloud_id), "\" ",\
                     "https://iam.api.cloud.yandex.net/iam/v1/tokens"))

IAM_TOKEN = subprocess.check_output(get_token,  shell=True)
IAM_TOKEN = str(IAM_TOKEN[16:-49])[2:-1] 

export_req = ''.join(("export IAM_TOKEN=", IAM_TOKEN ))
to_curl = ''.join(("curl -X POST -H \"Content-Type: application/json\" -H \"Authorization: Bearer ", \
                   IAM_TOKEN, \
                   "\" -d @body.json https://vision.api.cloud.yandex.net/vision/v1/batchAnalyze > output.json"))

# Get answer
os.system(export_req)
os.system(to_curl)

#YandexVisions answer in output.json