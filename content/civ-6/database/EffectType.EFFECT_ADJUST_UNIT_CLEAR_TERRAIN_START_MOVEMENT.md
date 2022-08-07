---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_CLEAR_TERRAIN_START_MOVEMENT
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_CLEAR_TERRAIN_START_MOVEMENT
>
> * Class: `UNITS`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="HEAVYCHARIOT_FASTER_CLEAR_TERRAIN"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"HEAVYCHARIOT_FASTER_CLEAR_TERRAIN",
		"MODIFIER_PLAYER_UNIT_ADJUST_CLEAR_TERRAIN_START_MOVEMENT"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"HEAVYCHARIOT_FASTER_CLEAR_TERRAIN",
		"Amount",
		1
	);
	
```

