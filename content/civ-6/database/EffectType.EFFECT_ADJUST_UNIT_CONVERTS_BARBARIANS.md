---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_CONVERTS_BARBARIANS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_CONVERTS_BARBARIANS
>
> * Class: `UNITS`
> * Parameters:
>	* Converts `Boolean`

## Samples

```SQL {title="APOSTLE_BARBARIAN_CONVERSION"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"APOSTLE_BARBARIAN_CONVERSION",
		"MODIFIER_PLAYER_UNIT_ADJUST_CONVERTS_BARBARIANS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"APOSTLE_BARBARIAN_CONVERSION",
		"Converts",
		1
	);
	
```

