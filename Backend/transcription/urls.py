from django.urls import path
from transcription.controllers import role_controller,user_controller 

urlpatterns = [
    # USER URLs
    path('users/', user_controller.getUsers),
    path('users/create/', user_controller.addUser),
    path('users/read/<int:pk>/', user_controller.getUser),
    path('users/update/<int:pk>/', user_controller.updateUser),
    path('users/delete/<int:pk>/', user_controller.deleteUser),

    # ROLE URLs
    path('roles/', role_controller.getRoles),
    path('roles/create/', role_controller.addRole),
    path('roles/read/<int:pk>/', role_controller.getRole),
    path('roles/update/<int:pk>/', role_controller.updateRole),
    path('roles/delete/<int:pk>/', role_controller.deleteRole)
]

