---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_WMD_PROTECTION
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_WMD_PROTECTION
>
> * Class: `UNITS`
> * Parameters:
>	* Blast `Integer`
>		* Percentage of resistance to damage from a WMD blast.
>	* Fallout `Integer`
>		* Percentage value of resistance to damage from WMD fallout.

## Samples
```SQL {title="GDR_WMD_RESISTANCE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"GDR_WMD_RESISTANCE",
		"MODIFIER_PLAYER_UNIT_ADJUST_WMD_RESISTANCE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"GDR_WMD_RESISTANCE",
		"Blast",
		50
	),
	(
		"GDR_WMD_RESISTANCE",
		"Fallout",
		100
	);
	
```

