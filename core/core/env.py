import environ 
from django.core.exceptions import ImproperlyConfigured


root = environ.Path(__file__) - 3  # get root of the project
env = environ.Env()
environ.Env.read_env()  # reading .env file
 
# Error handler function for get env
def get_env_value(env_variable):
	try:
		return env.str(env_variable)
	except KeyError:
		error_msg = 'Set the {} environment variable'.format(env_variable)
		raise ImproperlyConfigured(error_msg)
