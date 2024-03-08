from starlette.datastructures import UploadFile
from tempfile import NamedTemporaryFile
import magic

async def analyze_content(file: UploadFile):
    content = await file.read()
    await file.close()

    temp = NamedTemporaryFile(delete=False)
    temp.write(content)
    temp.close()
    
    return magic.from_file(temp.name, mime=True)