#!/usr/bin/env python2
# -*- coding: UTF-8 -*-


class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = '?\xbf,\xb4\x8d\xa3"<\x9c\xb0@\x0f5\xab,w\xee\x8d$0\x13\x8b83'

    @staticmethod
    def init_app():
        pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    pass


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'Production': ProductionConfig,
    'default': DevelopmentConfig
}
