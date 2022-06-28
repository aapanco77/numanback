# import email
# import pytest

# from apps.usuario.models import Usuario

# @pytest.mark.django_db
# def test_commonuser_creation():
#     user = Usuario.objects.create_user(
#         username='beyonder'
#         email='beyonder@gmail.com'
#         nombres='Juanelo Sanchito'
#         password='12345'
#         is_staff=False
#     )

#     assert user.username == 'beyonder'

# @pytest.mark.django_db
# def test_superuser_creation():
#     user = Usuario.objects.create_superuser(
#         username='beyonder'
#         email='beyonder@gmail.com'
#         nombres='Juanelo Sanchito'
#         password='12345'
#     )

#     assert user.is_superuser


# @pytest.mark.django_db
# def test_staff_user_creation():
#     user = Usuario.objects.create_user(
#         username='beyonder'
#         email='beyonder@gmail.com'
#         nombres='Juanelo Sanchito'
#         password='12345'
#         is_staff=True
#     )

#     assert user.is_staff