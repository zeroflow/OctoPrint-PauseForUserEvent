# OctoPrint-Terminaltoevent

When "echo:busy: paused for user" is received on the serial port, this plugin then raises a "paused_for_user" event, which may then be used with other plugins like mqtt to alert the user, that the printer is paused and needs attention

The primary use for this is the Prusa MMU2S, which when it fails to load/unload filament, will halt the printer and send this message on serial.

## Setup

Install via the bundled [Plugin Manager](https://github.com/foosel/OctoPrint/wiki/Plugin:-Plugin-Manager)
or manually using this URL:

    https://github.com/zeroflow/OctoPrint-PauseForUserEvent/archive/master.zip

## Configuration

No configuration
