import yaml
import pika

# read in the contents of the config file
with open('../config.yaml', 'r') as f:
	config = yaml.safe_load(f)
	f.close()

# function returns the parameters to connect to the rabbitmq server
def get_params():
	cred = pika.PlainCredentials(config['rabbitmq']['username'], config['rabbitmq']['password'])
	params = pika.ConnectionParameters(config['rabbitmq']['host'], config['rabbitmq']['port'], config['rabbitmq']['v-host'], cred)
	return params