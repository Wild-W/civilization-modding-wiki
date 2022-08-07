---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_ADVANCED_COASTAL_RAID
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_ADVANCED_COASTAL_RAID
>
> * Class: `UNITS`
> * Parameters:
>	* UseAdvancedCoastalRaid `Boolean`

## Samples
```SQL {title="CORSAIR_LESS_MOVEMENT_RAID"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"CORSAIR_LESS_MOVEMENT_RAID",
		"MODIFIER_PLAYER_UNIT_ADJUST_ADVANCED_COASTAL_RAID"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"CORSAIR_LESS_MOVEMENT_RAID",
		"UseAdvancedCoastalRaid",
		1
	);
	
```

