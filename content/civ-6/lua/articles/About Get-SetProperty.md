---
title: "About Get-SetProperty"
tags:
- civ6/articles/lua
---
# Get/SetProperty

> these methods expect an implicit "self" argument. invoke them with `:`
-----
## Usage
> `Data [any]` [Object]:GetProperty( `Key: string` )

> `nil` [Object]:SetProperty( `Key: string`, `Data [any]` )


Get/SetProperty is a useful little method that can be used to store persistent data in [](Lua#Instances%7CInstances) and in the [Game](civ-6/lua/Game.md) object. Simply provide the key and the data to store with SetProperty, or just the key to retrieve it with GetProperty.

Get/SetProperty always expects an implicit self argument and MUST be called with `:`, even on the Game object.

Properties stored this way are tied to the save file and will persist when the game is closed and the save is reloaded. Properties are accessible by all scripts in all contexts: you can save the data in a Gameplay script in one mod, and load it from a UI script in another mod: which makes it important that the keys you use are unique to your mod.

The method can store a large variety of different data types, but notably it can also store Lua tables! So you don't have to store every separate piece of data under a separate key.

### Related Methods
Lua
  > `table<Key: string, Data [any]>` Object:GetProperties( )

  > Events.[Object]PropertyChanged( `Params [...]` )

DB
  > REQUIREMENT_PLOT_PROPERTY_MATCHES( `PropertyName: string`, `PropertyMinimum: string|number` )

  > EFFECT_ASSIGN_Object_PROPERTY( `PropertyName: string` )

  > EFFECT_ADJUST_Object_PROPERTY( `PropertyName: string` )

------------
[^1]: This is an article on using Lua in [Civilization 6 ](civ-6/lua/articles/articles-index)
