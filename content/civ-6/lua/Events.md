---
title: "Events"
tags:
- Events
---

# Events
## Usage
Events can be used to trigger functions that are "added" to them. Events can be added to in two ways: `GameEvents.SomeEvent.Add(SomeFunction)` or  `Events.SomeEvent.Add(SomeFunction)`.  All events can be added to with `GameEvents`, but some do not exist in `Events`. And while all events DO exist in `GameEvents`, they may not fire correctly if they also exist in `Events` 

For ease of reference, it will be noted on the individual event pages whether an event has been used by Firaxis with Events, GameEvents, or not at all.

Event titles will be prefixed with GameCoreEvent, LocalMachineEvent, SerialEvent, or SequenceEvent. This information has been scraped from the game's binaries does not seem to have any impact on actual usage. Though it may give clues on how it is *supposed* to be used.