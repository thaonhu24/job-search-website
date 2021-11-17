from io import FileIO
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.base import Model
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.generic.base import View
import datetime

from .models import Profile as ProfileModel

UserModel = get_user_model()
class Profile(LoginRequiredMixin, View):
      def get(self, request):
            try:
                  user = UserModel.objects.get(username=request.user)
                  profile = ProfileModel.objects.get(user=request.user)
            except UserModel.DoesNotExist:
                  return render(request, 'profiles/JobSeeker/profile.html', {'username': 'Unknown'})
            context = {
                  'user': user,
                  'profile': profile,
            }
            return render(request, 'profiles/JobSeeker/profile.html', context)

      def post(self, request, *args, **kwargs):
            if request.method == 'POST' and request.is_ajax():
                  # Get username of user
                  username = request.user
                  print(request.POST)
                  try:
                        instance = ProfileModel.objects.get(user=username)
                  except ProfileModel.DoesNotExist:
                        instance = ProfileModel.objects.create(user=username)
                  if request.POST.get('form') == 'basicInformationForm':
                        # Get all field date of POST
                        full_name = request.POST.get('full_name') if request.POST.get('full_name') else None
                        phone_number = request.POST.get('phone_number') if request.POST.get('phone_number') else None
                        address = request.POST.get('address') if request.POST.get('address') else None
                        gender = request.POST.get('gender') if request.POST.get('gender') else None
                        date_of_birth = request.POST.get('date_of_birth') if request.POST.get('date_of_birth') else None
                        # Update fields in Profile model
                        if full_name:
                              instance.full_name = full_name
                        if phone_number:
                              instance.phone_number = phone_number
                        if address:
                              instance.address = address
                        if gender:
                              instance.gender = gender
                        # Handle with datetime type 
                        date_string = date_of_birth
                        date_format = '%Y-%m-%d'
                        try:
                              date_obj = datetime.datetime.strptime(date_string, date_format)
                        except ValueError:
                              print("Incorrect date format, should be YYYY-MM-DD")
                        try: 
                              instance.date_of_birth = date_obj
                        except ValueError:
                              print('Cannot save date to model')
                        
                        # Save all things which are just updated
                        instance.save()

                        return JsonResponse({
                              'full_name': instance.full_name,
                              'phone_number': instance.phone_number,
                              'address': instance.address,
                              'gender': instance.gender,
                              'date_of_birth': instance.date_of_birth,
                        }, safe=False, content_type='application/json')

                  if request.POST.get('form') == 'changeProfilePicture':
                        img = request.FILES.get('image') if request.FILES.get('image') else None
                        if img:
                              instance.profile_picture = img
                        instance.save()
                        return JsonResponse({ 'message': 'Uploaded'}, safe=False)
                  if request.POST.get('form') == 'summaryForm':
                        summary = request.POST.get('summary') if request.POST.get('summary') else None
                        if summary:
                              instance.summary = summary
                        instance.save()
                        return JsonResponse({
                              'summary': instance.summary,
                        }, safe=False, content_type='application/json')
                  if request.POST.get('form') == 'educationForm':
                        # Get all field date of POST
                        name_of_school = request.POST.get('name_of_school') if request.POST.get('name_of_school') else None
                        academic_degree = request.POST.get('academic_degree') if request.POST.get('academic_degree') else None
                        name_of_major = request.POST.get('name_of_major') if request.POST.get('name_of_major') else None
                        time_admission = request.POST.get('time_admission') if request.POST.get('time_admission') else None
                        time_graduate = request.POST.get('time_graduate') if request.POST.get('time_graduate') else None
                        is_studying = True if request.POST.get('is_studying') == '1' else False
                        additional_education = request.POST.get('additional_education') if request.POST.get('additional_education') else None
                        # Update fields in Profile model
                        if name_of_school:
                              instance.name_of_school = name_of_school.strip()
                        if academic_degree:
                              instance.academic_degree = academic_degree.strip()
                        if name_of_major:
                              instance.name_of_major = name_of_major.strip()
                         # Handle with datetime type 
                        if time_admission:
                              date_string = time_admission
                              date_format = '%Y-%m-%d'
                              try:
                                    date_obj = datetime.datetime.strptime(date_string, date_format)
                              except ValueError:
                                    print("Incorrect date format, should be YYYY-MM-DD")
                              try: 
                                    instance.time_admission = date_obj
                              except ValueError:
                                    print('Cannot save date to model')
                        if time_graduate:
                              date_string = time_graduate
                              date_format = '%Y-%m-%d'
                              try:
                                    date_obj = datetime.datetime.strptime(date_string, date_format)
                              except ValueError:
                                    print("Incorrect date format, should be YYYY-MM-DD")
                              try: 
                                    instance.time_graduate = date_obj
                              except ValueError:
                                    print('Cannot save date to model')
                        if is_studying:
                              instance.is_studying = is_studying
                        if additional_education:
                              instance.additional_education = additional_education.strip()
                        instance.save()
                        return JsonResponse({
                              'name_of_school': instance.name_of_school,
                              'academic_degree': instance.academic_degree,
                              'name_of_major': instance.name_of_major,
                              'time_admission': instance.time_admission,
                              'time_graduate': instance.time_graduate,
                              'is_studying': instance.is_studying,
                              'additional_education': instance.additional_education
                        }, safe=False, content_type='application/json')
            return JsonResponse({'error': 'Submit error --------------', }, safe=False)
      
class RecruiterProfile(LoginRequiredMixin, View):
      def get(self, request):
            return render(request, 'profiles/Recruiter/profile.html')
