---
title: "About HavokScript"
tags:
- civ6/articles/lua
---
# HavokScript

> HavokScript is a superset of Lua 5.1 and is Civ VI’s primary scripting language; its purported benefits are faster performance and type safety
-----
HavokScript extends Lua with:
- Statically typed variables
- Structs
    - Keyword: hstructure
    - Keyword: hmake

HavokScript features are entirely optional and most modders completely ignore them, but they are often used by Firaxis and knowing about them, even if you choose not to use them may help your understanding of Civ’s Lua environment.

-----

### *What are statically typed variables?*

Statically typed variables are variables with types determined at run-time. Unlike dynamically typed variables, statically typed variables cannot be assigned a value of another type.

### *Why use statically typed variables?*

Statically typing variables is primarily helpful for debugging and code organization, but will also provide a minor performance increase. Any attempt to set a statically typed variable to a value of another type is considered a syntax error and will be recognized immediately by the interpreter.

### *Why not use statically typed variables?*

They aren’t standard lua syntax so your IDE will detect them as syntax errors, which defeats their code organizing purpose and really screws with Intellisense.


### **Code example:**

```lua
local x: number = 30
local y: string = "I am a string"

x = y
```

> <span style="color:tomato">Syntax Error: [string "local x: number = 30 local y: string = "I am a string" x = y"]:4: Attempting to set local variable of type 'number' to type 'string'</span>

-----

### *What are structs?*

To put it simply, structs are strict templates for tables, they force you to obey a structure of fields and data types.

### *Why use structs?*

Structs are useful for when you find yourself managing a particularly large script or codebase where consistently structured tables are constantly being passed around and there is a concern for performance.

### *Why not use structs?*

The gains in performance that structs provide come at the cost of the dynamic nature of Lua’s tables, and to be frank, most mods don’t warrant a need for them. Using structs where it’s unnecessary will only serve to complicate your code, and their unique syntax will be highlighted as an error in your IDE.

### **Code examples:**

```lua
hstructure AdvisorItem
	Message: string;--TXT key to look up for advisor message
	MessageAudio: string;--Name of audio to play with message
	Image: string;--(optional) Name of texture used in image
	OptionsNum: number;--Number of options
	Button1Text: string;--TXT key to look up for button 1
	Button2Text: string;--" " " 2
	Button1Func: ifunction;--Callback on button 1
	Button2Func: ifunction;--" " " 2
	CalloutHeader: string;--TXT key to look up for callout header
	CalloutBody: string;--TXT key to look up for callout body
	PlotCallback: ifunction;--Returns plotID of dialog’s plot
	ShowPortrait: boolean;--Will advisor portrait appear in dialog?
	UITriggers: table;--IDs/Trigger names when advisor item is up
end
```

This struct which can be found in AdvisorPopup.lua defines the structure of data used to create advisor popup messages. Throughout the file, functions are defined for handling such structs, such as this:

```lua
function ShowOrQueuePopup(advisorData: AdvisorItem)
	--Code here
end
```

This function expects an AdvisorItem, which can be created like so:

```lua
local exampleAdvisorItem = hmake AdvisorItem {
	Message = "message text not set",
	MessageAudio = nil,
	OptionsNum = 0,
	Button1Text = "button1 text not set",
	Button2Text = nil,
	Button1Func = nil,
	Button2Func = nil,
	CalloutHeader = "header text not set",
	CalloutBody = "body text not set",
	PlotCallback = nil,
	ShowPortrait = false,
	UITriggers = {} 
};
```

Or alternatively you can omit entries you intend to init as nil:

```lua
local exampleAdvisorItem = hmake AdvisorItem {
	Message = "message text not set",
	OptionsNum = 0,
	Button1Text = "button1 text not set",
	CalloutHeader = "header text not set",
	CalloutBody = "body text not set",
	ShowPortrait = false,
	UITriggers = {} 
};

--But you can still set them later
exampleAdvisorItem.Button2Text = "Hello World!"
```

Most interestingly, hstructures will remain defined for the entire lifespan of the application and become accessible from any context, even the front-end and in-game.

------------
[^1]: This is an article on using Lua in [Civilization 6 ](civ-6/lua/articles/articles-index)
