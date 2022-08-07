---
tags:
- EffectType
title: EFFECT_ADJUST_GLOBAL_WMD_STOCKPILE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_GLOBAL_WMD_STOCKPILE
>
> * Class: `Unknown`
> * Parameters:
>	* Amount `Integer`
>		* Value to set the target player's WMD count(s) to.
>	* TargetOnly `Boolean`
>		* If set to true\, effect only applies to the target player. If false\, effect applies to all players based on the number of WMDs the target player has.

## Samples

```SQL {title="PLAYER_TARGET_WMD_BAN"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"PLAYER_TARGET_WMD_BAN",
		"MODIFIER_PLAYERS_ADJUST_WMD_STOCKPILE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"PLAYER_TARGET_WMD_BAN",
		"Amount",
		0
	),
	(
		"PLAYER_TARGET_WMD_BAN",
		"TargetOnly",
		1
	);
	
```

