#!/usr/bin/python3

import os
import pyinotify

import importlib
import noahs_module


class EventProcessor(pyinotify.ProcessEvent):
    _methods = ["IN_CREATE",
                "IN_OPEN",
                "IN_ACCESS",
                "IN_ATTRIB",
                "IN_CLOSE_NOWRITE",
                #"IN_CLOSE_WRITE",
                "IN_DELETE",
                "IN_DELETE_SELF",
                "IN_IGNORED",
                "IN_MODIFY",
                "IN_MOVE_SELF",
                "IN_MOVED_FROM",
                "IN_MOVED_TO",
                "IN_Q_OVERFLOW",
                "IN_UNMOUNT",
                "default"]

def process_generator(cls, method):
    def _method_name(self, event):
        print("Method name: process_{}()\n"
               "Path name: {}\n"
               "Event Name: {}\n".format(method, event.pathname, event.maskname))
    _method_name.__name__ = "process_{}".format(method)
    setattr(cls, _method_name.__name__, _method_name)


def process_IN_CLOSE_WRITE():
    print("test")

def noahs_proc_gen(cls, method):
    def _method_name(self, event):
        
        print("noah: Method name: process_{}()\n"
               "Path name: {}\n"
               "Event Name: {}\n".format(method, event.pathname, event.maskname))
        importlib.reload( noahs_module )
        noahs_module.doSomething( 1.0 )
               
    _method_name.__name__ = "process_{}".format(method)

             
    setattr(cls, _method_name.__name__, _method_name)


for method in EventProcessor._methods:
    process_generator(EventProcessor, method)

noahs_proc_gen( EventProcessor, "IN_CLOSE_WRITE" );

watch_manager = pyinotify.WatchManager()
event_notifier = pyinotify.Notifier(watch_manager, EventProcessor())

watch_this = os.path.abspath("../notification_dir")
watch_manager.add_watch(watch_this, pyinotify.ALL_EVENTS)
event_notifier.loop()



