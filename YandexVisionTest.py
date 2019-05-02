# YandexVision using experience
# only free options (Images classificayion & Face detection)
# read more https://cloud.yandex.ru/services/vision

import base64
import json
import os

# modificated recomended function  https://cloud.yandex.ru/docs/vision/operations/face-detection/ (in Python)
def encode_file(file):
    with open(file, 'rb') as f:
        file_content = f.read()
    return base64.b64encode(file_content).decode('utf-8')

outfile = encode_file('017.jpg') #my image file 

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
    
    
os.system("export IAM_TOKEN=CggaATEVAgAAABKABAmHyQyUryuNBxImeEXEMjQenTouwzPqe3HtKMQt4qn1FZC5xmmKk7D5wGP6lO_yELat_ot41acarBq_vXsCW9XIGXOIw-_4kK8Dqh9D8bBqrPZTYIumLGrnCqtzygL9pNSui_oo4pGv3aJrF9F4PTuNBXbbiYvGVjhn1m8uyF_hmhup9Nt5jvwlp741_QcL_eWnMkbY0_tmp2GHYdF3qz6UCE_n1SERstFTxy4Qg4YIH22rqqxC0aAcPS_ChC5sO3X53NroGYNWCBBB6XJtc5tjfL7E1UcXOIxtF0XhYCSpCvrUU8IKYDrQicN9lKk1L__ZASr7OeyrBg5nc4ZX0ZtRITbVk3ut6Du7qCOEzotDyoKxiIMKqRngf6OR6EjDWT-CW1ExSFpmAUkm109ANmVYsBk9FwhO74V_sZg6VdI2ef2-graxkjMWvCZVPny3rtAlP5TTtChiK9J8wir4XSiO48IAzmqKKnK7zLVo3szlt3J0zg_AyWtPYN4UpWuAx5WAOg3WOWPjwXtj-AJUWAIlnXX54P6RnhzMNxsU2ovr6bxiTF-HQdTnVohF2odWqa5g5COb7FkWacmLs8ztDOimEVhlxR33CBqUQwwQ0seomSBfxsrPqgDtRDN2SDrUHH_VP1h_NTdZeEfGGQqg9oe39rQufw2QKBY93ZvLvbNTGmMKIDI5NWMxYzU0NjZlYTQ4OGM4OTNiZGZiYjRmNmI5NWNhEJqlrOYFGNr2ruYFIiEKFGFqZWZhMWYwanBkcTVnMTBvNWEwEglpLWxhbmNpbmdaADACOAFKCBoBMRUCAAAAUAEg8gQCggaATEVAgAAABKABAmHyQyUryuNBxImeEXEMjQenTouwzPqe3HtKMQt4qn1FZC5xmmKk7D5wGP6lO_yELat_ot41acarBq_vXsCW9XIGXOIw-_4kK8Dqh9D8bBqrPZTYIumLGrnCqtzygL9pNSui_oo4pGv3aJrF9F4PTuNBXbbiYvGVjhn1m8uyF_hmhup9Nt5jvwlp741_QcL_eWnMkbY0_tmp2GHYdF3qz6UCE_n1SERstFTxy4Qg4YIH22rqqxC0aAcPS_ChC5sO3X53NroGYNWCBBB6XJtc5tjfL7E1UcXOIxtF0XhYCSpCvrUU8IKYDrQicN9lKk1L__ZASr7OeyrBg5nc4ZX0ZtRITbVk3ut6Du7qCOEzotDyoKxiIMKqRngf6OR6EjDWT-CW1ExSFpmAUkm109ANmVYsBk9FwhO74V_sZg6VdI2ef2-graxkjMWvCZVPny3rtAlP5TTtChiK9J8wir4XSiO48IAzmqKKnK7zLVo3szlt3J0zg_AyWtPYN4UpWuAx5WAOg3WOWPjwXtj-AJUWAIlnXX54P6RnhzMNxsU2ovr6bxiTF-HQdTnVohF2odWqa5g5COb7FkWacmLs8ztDOimEVhlxR33CBqUQwwQ0seomSBfxsrPqgDtRDN2SDrUHH_VP1h_NTdZeEfGGQqg9oe39rQufw2QKBY93ZvLvbNTGmMKIDI5NWMxYzU0NjZlYTQ4OGM4OTNiZGZiYjRmNmI5NWNhEJqlrOYFGNr2ruYFIiEKFGFqZWZhMWYwanBkcTVnMTBvNWEwEglpLWxhbmNpbmdaADACOAFKCBoBMRUCAAAAUAEg8gQ")
os.system("curl -X POST -H \"Content-Type: application/json\" -H \"Authorization: Bearer CggaATEVAgAAABKABAmHyQyUryuNBxImeEXEMjQenTouwzPqe3HtKMQt4qn1FZC5xmmKk7D5wGP6lO_yELat_ot41acarBq_vXsCW9XIGXOIw-_4kK8Dqh9D8bBqrPZTYIumLGrnCqtzygL9pNSui_oo4pGv3aJrF9F4PTuNBXbbiYvGVjhn1m8uyF_hmhup9Nt5jvwlp741_QcL_eWnMkbY0_tmp2GHYdF3qz6UCE_n1SERstFTxy4Qg4YIH22rqqxC0aAcPS_ChC5sO3X53NroGYNWCBBB6XJtc5tjfL7E1UcXOIxtF0XhYCSpCvrUU8IKYDrQicN9lKk1L__ZASr7OeyrBg5nc4ZX0ZtRITbVk3ut6Du7qCOEzotDyoKxiIMKqRngf6OR6EjDWT-CW1ExSFpmAUkm109ANmVYsBk9FwhO74V_sZg6VdI2ef2-graxkjMWvCZVPny3rtAlP5TTtChiK9J8wir4XSiO48IAzmqKKnK7zLVo3szlt3J0zg_AyWtPYN4UpWuAx5WAOg3WOWPjwXtj-AJUWAIlnXX54P6RnhzMNxsU2ovr6bxiTF-HQdTnVohF2odWqa5g5COb7FkWacmLs8ztDOimEVhlxR33CBqUQwwQ0seomSBfxsrPqgDtRDN2SDrUHH_VP1h_NTdZeEfGGQqg9oe39rQufw2QKBY93ZvLvbNTGmMKIDI5NWMxYzU0NjZlYTQ4OGM4OTNiZGZiYjRmNmI5NWNhEJqlrOYFGNr2ruYFIiEKFGFqZWZhMWYwanBkcTVnMTBvNWEwEglpLWxhbmNpbmdaADACOAFKCBoBMRUCAAAAUAEg8gQ\" -d @body.json https://vision.api.cloud.yandex.net/vision/v1/batchAnalyze > output.json")