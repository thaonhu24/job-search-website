from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.shortcuts import render

from posts.models import Post
from accounts.models import User
from profiles.models import Profile
from profiles.models import RecruiterProfile
from posts.models import Post_apply

@login_required
def managePost(request):
    recruiter_profile = RecruiterProfile.objects.get(user=request.user)
    context = {
        'profile_picture_company_link': recruiter_profile.profile_picture_company.url,
        'Posts': Post.objects.filter(author_id=request.user.id).order_by('-time_create')
    }
    return render(request,'manage-posts.html', context)

def manageApplicant(request):
    post=Post.objects.filter(author_id=request.user.id)
    print(post)
    listpost=[]
    list_cant=[]
    for i in post:
        p=Post_apply.objects.filter(post_apply_id=i.id,status_apply="wait_accept")
        if len(p)>0:
            listpost.append(list(p))
   
    
    arr=list()
    for i in listpost:
        
        for j in i:
            
            item= Profile.objects.filter(user_id=j.user_apply_id).first()
            if item!=None:
                d={
                    "full_name":item.full_name,
                    "name_of_interested_job":item.name_of_interested_job,
                    "address":item.address,
                    "previous_job_title":item.previous_job_title,
                    "name_of_previous_company":item.name_of_previous_company,
                    "time_start_previous_job":item.time_start_previous_job,
                    "time_end_previous_job":item.time_end_previous_job,
                    "name_of_school":item.name_of_school,
                    "profile_picture":item.profile_picture.url,
                    "id_post":j.post_apply_id,
                    "user_id":item.user_id,
                    "id_apply":j.id
                }
                arr.append(d)
    list_cant.append(arr)
    
    
    return render(request,'manage-candidate.html',{
        'list_job':post,
        'list_candidate':list_cant,
        "disable":" "
        })

def accept(request):
    if request.method == "POST":
        idApply = request.POST.get("idApply")
        print(idApply)
        p = Post_apply.objects.update_or_create(id=idApply, defaults={"status_apply":"accepted"})
        print(p)
        return JsonResponse({
            "data":"Ch???p nh???n ???ng vi??n th??nh c??ng!!!",
            "status":"accepted"
            }, safe=False, content_type='application/json')
    return JsonResponse({
        "data":"Kh??ng th??nh c??ng, ???? g???p l???i"
        }, safe=False, content_type='application/json')    

def refuse(request):
    if request.method == "POST":
        idApply = request.POST.get("idApply")[5:]
        print(idApply)
        p=Post_apply.objects.update_or_create(id=idApply, defaults={"status_apply":"refuse"})
        return JsonResponse({
            "data":"T??? ch???i ???ng vi??n th??nh c??ng!!!",
            "status":"refused"
        })
    return JsonResponse({
        "data":"Kh??ng th??nh c??ng, ???? g???p l???i"
        }, safe=False, content_type='application/json')      

   

def listAccepted(request):
    post=Post.objects.filter(author_id=request.user.id)
    listpost=[]
    list_cant=[]
    for i in post:
        p=Post_apply.objects.filter(post_apply_id=i.id,status_apply="accepted")
        
        if len(p)>0:
            listpost.append(list(p))
   
    
    arr=list()
    for i in listpost:
        for j in i:
            
            item= Profile.objects.filter(user_id=j.user_apply_id).first()
            
            if item!=None:
                d={
                    "full_name":item.full_name,
                    "name_of_interested_job":item.name_of_interested_job,
                    "address":item.address,
                    "previous_job_title":item.previous_job_title,
                    "name_of_previous_company":item.name_of_previous_company,
                    "time_start_previous_job":item.time_start_previous_job,
                    "time_end_previous_job":item.time_end_previous_job,
                    "name_of_school":item.name_of_school,
                    "profile_picture":item.profile_picture.url,
                    "id_post":j.post_apply_id,
                    "user_id":item.user_id,
                    "id_apply":j.id
                }
                arr.append(d)
    list_cant.append(arr)
    # print(list_cant)
    return render(request,'manage-candidate.html',{
        'list_job':post,
        'list_candidate':list_cant,
        "disable":"disabled"
        })


def listRefuse(request):
    post=Post.objects.filter(author_id=request.user.id)
    listpost=[]
    list_cant=[]
    for i in post:
        p=Post_apply.objects.filter(post_apply_id=i.id,status_apply="refuse")
        if len(p)>0:
            listpost.append(list(p))
   
    
    arr=list()
    for i in listpost:
        
        for j in i:
            
            item= Profile.objects.filter(user_id=j.user_apply_id).first()
            print(item)
            if item!=None:
                d={
                    "full_name":item.full_name,
                    "name_of_interested_job":item.name_of_interested_job,
                    "address":item.address,
                    "previous_job_title":item.previous_job_title,
                    "name_of_previous_company":item.name_of_previous_company,
                    "time_start_previous_job":item.time_start_previous_job,
                    "time_end_previous_job":item.time_end_previous_job,
                    "name_of_school":item.name_of_school,
                    "profile_picture":item.profile_picture.url,
                    "id_post":j.post_apply_id,
                    "user_id":item.user_id,
                    "id_apply":j.id
                }
                arr.append(d)
    list_cant.append(arr)
    return render(request,'manage-candidate.html',{
        'list_job':post,
        'list_candidate':list_cant,
        "disable":"disabled"
        })                  
