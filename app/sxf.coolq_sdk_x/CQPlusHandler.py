# -*- coding:utf-8 -*-

import cqplus


class MainHandler(cqplus.CQPlusHandler):
    def handle_event(self, event, params):
        self.logging.debug("hello world")