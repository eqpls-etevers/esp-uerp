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

from schema.adapter.vmware.docs import Knowledgebase
from schema.adapter.atlassian.confluence import Space, Page
from schema.adapter.wolken import Ticket


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
        await self.registerModel(Space)
        await self.registerModel(Page)
        await self.registerModel(Knowledgebase)
        await self.registerModel(Ticket)

    async def shutdown(self): pass
