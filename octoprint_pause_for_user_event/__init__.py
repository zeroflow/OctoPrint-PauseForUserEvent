# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin
import logging
from octoprint.events import eventManager, Events

class PauseForUserEvent(octoprint.plugin.SettingsPlugin):
    
    def get_settings_defaults(self):
        return {}
        
    def get_update_information(self):
        # Define the configuration for your plugin to use with the Software Update
        # Plugin here. See https://github.com/foosel/OctoPrint/wiki/Plugin:-Software-Update
        # for details.
        return dict(
            PauseForUserEvent=dict(
                displayName="PauseForUser Event Plugin",
                displayVersion=self._plugin_version,

                # version check: github repository
                type="github_release",
                user="zeroflow",
                repo="OctoPrint-PauseForUserEvent",
                current=self._plugin_version,

                # update method: pip
                pip="https://github.com/zeroflow/OctoPrint-PauseForUserEvent/archive/{target_version}.zip"
            )
        )
    
    def on_after_startup(self):
        self.triggered = False
        None
        
    def register_custom_events(self, *args, **kwargs):
        return ["notify"]
    
    def recv_callback(self, comm_instance, line, *args, **kwargs):
        # Found keyword, fire event and block until other text is received
        if "echo:busy: paused for user" in line:
            if not self.triggered:
                eventManager().fire(Events.PLUGIN_PAUSE_FOR_USER_EVENT_NOTIFY)
                self.triggered = True
        # Other text, we may fire another event if we encounter "paused for user" again
        else:
            self.triggered = False
            
        return line

# If you want your plugin to be registered within OctoPrint under a different name than what you defined in setup.py
# ("OctoPrint-PluginSkeleton"), you may define that here. Same goes for the other metadata derived from setup.py that
# can be overwritten via __plugin_xyz__ control properties. See the documentation for that.
__plugin_name__ = "PauseForUserEvent Plugin"

def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = PauseForUserEvent()

    global __plugin_hooks__
    __plugin_hooks__ = {
        "octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information,
        "octoprint.comm.protocol.gcode.received": __plugin_implementation__.recv_callback,
        "octoprint.events.register_custom_events": __plugin_implementation__.register_custom_events
    }

