class Config(object):

	DEBUG = True


class DevelopmentConfig(Config):
	"""
	Development configurations
	"""

	DEBUG = True
	SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
	"""
	Production condigurations
	"""

	DEBUG = False

class TestingConfig(Config):
    	"""
    	Testing configurations
    	"""

    	TESTING = True

app_config = {
	'development': DevelopmentConfig,
	'production': ProductionConfig,
	'testing': TestingConfig
}
