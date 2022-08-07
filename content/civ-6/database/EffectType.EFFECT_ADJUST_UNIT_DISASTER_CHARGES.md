---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_DISASTER_CHARGES
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_DISASTER_CHARGES
>
> * Class: `UNITS`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="SOOTHSAYER_CHARGES"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"SOOTHSAYER_CHARGES",
		"MODIFIER_UNIT_ADJUST_DISASTER_CHARGES"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"SOOTHSAYER_CHARGES",
		"Amount",
		1
	);
	
```

