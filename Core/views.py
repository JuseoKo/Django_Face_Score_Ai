from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .ai import Ai

def uploadFile(request):
    if request.method == "POST":
        #데이터 받음
        uploadedFile = request.FILES["uploadedFile"]
        #파일저장
        fs = FileSystemStorage()
        filename = fs.save(uploadedFile.name, uploadedFile)
        uploaded_file_url = fs.url(filename)
        #Ai
        score = Ai("/Users/maria/Desktop/Code/DjangoFileUpload _V2" + uploaded_file_url)
        room_num = round(float(score), 0)

        return render(request, "chat/index.html", {'uploaded_file_url': uploaded_file_url, 'score': score, 'room_num': room_num})
    else:
        return render(request, "Core/upload-file.html")