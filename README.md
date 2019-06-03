
# OctoPrint-PauseForUserEvent

When `echo:busy: paused for user` is received on the serial port, this plugin then raises a `paused_for_user` event, which may then be used with other plugins like [OctoPrint-MQTT](https://github.com/OctoPrint/OctoPrint-MQTT) to alert the user, that the printer needs attention.

The primary use for this is the Prusa MMU2S, which when it fails to load/unload filament, will halt the printer and send this message on serial.

For example, this is, what an unsuccesful loading procedure looks like:

    Send: T1*62
    
    mmu_get_response - begin move: T-code
    MMU <= 'T1'
    Unloading finished 2
    mmu_get_response - begin move: load
    echo:busy: processing
    echo:busy: processing
    MMU => 'ok'
    mmu_get_response() returning: 1
    echo:busy: processing
    MMU <= 'A'
    mmu_get_response - begin move: T-code
    MMU <= 'T1'
    Unloading finished 2
    mmu_get_response - begin move: load
    echo:busy: processing
    echo:busy: processing
    echo:busy: processing
    MMU <= 'A'
    MMU => 'ok'
    mmu_get_response() returning: 1
    echo:busy: processing
    mmu_get_response - begin move: unload
    MMU <= 'U0'
    Unloading finished 1
    echo:busy: processing
    echo:busy: processing
    MMU => 'ok'
    mmu_get_response() returning: 1
    echo:busy: paused for user
    echo:busy: paused for user
    echo:busy: paused for user
    echo:busy: paused for user
    echo:busy: paused for user
    echo:busy: paused for user

And then the printer waits until the user has fixed the issue and pressed the button on the LCD.

This plugin now raises an Event in OctoPrint when "echo:busy: paused for user" is received.

## Setup

Install via the bundled [Plugin Manager](https://github.com/foosel/OctoPrint/wiki/Plugin:-Plugin-Manager)
or manually using this URL:

    https://github.com/zeroflow/OctoPrint-PauseForUserEvent/archive/master.zip

## Configuration

No configuration
