# -*- coding: utf-8 -*-
'''
Equal Plus
@author: Hye-Churn Jang
'''

#===============================================================================
# Import
#===============================================================================
from common import UerpControl
from driver import Redis, ElasticSearch, PostgreSql
from schema.sample.model import Blog, Message
from schema.support.vmware.docs import Knowledgebase


#===============================================================================
# Implement
#===============================================================================
class Control(UerpControl):

    def __init__(self, api, config):
        UerpControl.__init__(
            self,
            api,
            config,
            cacheDriver=Redis,
            searchDriver=ElasticSearch,
            databaseDriver=PostgreSql
        )

    async def startup(self):
        
        await self.registerModel(
            Knowledgebase,
            version=1,
            cacheOptions={
                'expire': 86400
            }, searchOptions={
                'expire': 2419200
            })

    async def shutdown(self): pass
