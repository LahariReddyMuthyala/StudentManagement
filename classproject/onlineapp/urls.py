from django.contrib import admin
from django.urls import path
from onlineapp.views import *

urlpatterns = [
    path('test/', testview.test, name="test"),
    path('login/', LoginController.as_view(), name="login"),
    path('signup/', SignUpController.as_view(), name="signup"),
    path('logout/', logout_user, name="logout"),

    path('api/v1/colleges/', college_list, name="rest_colleges"),
    path('api/v1/colleges/<int:cpk>/', college_list, name="rest_colleges"),
    path('api/v1/colleges/<int:cpk>/students/', student_details.as_view(), name="rest_students"),
    path('api/v1/colleges/<int:cpk>/students/<int:spk>/', student_details.as_view(), name="rest_students"),
    path('api-token-auth/', CustomAuthToken.as_view()),

    path('colleges/', CollegeView.as_view(), name="colleges_html"),
    path('colleges/<int:college_id>/', CollegeView.as_view(), name="college_details"),
    path('colleges/add', AddCollegeView.as_view(), name="add_college"),
    path('colleges/<int:id>/edit', AddCollegeView.as_view(), name="edit_college"),
    path('colleges/<int:id>/delete', DeleteCollegeView.as_view(), name="delete_college"),
    path('colleges/<int:college_id>/addstudent', AddStudentView.as_view(), name="add_student"),
    path('colleges/<int:college_id>/editstudent/<int:student_id>', AddStudentView.as_view(), name="edit_student"),
    path('colleges/<int:college_id>/deletestudent/<int:student_id>', DeleteStudentView.as_view(), name="delete_student"),

]
