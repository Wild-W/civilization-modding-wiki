---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_EXPERIENCE_LEVEL
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_EXPERIENCE_LEVEL
>
> * Class: `UNITS`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="GDR_VETERAN_NAME"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"GDR_VETERAN_NAME",
		"MODIFIER_PLAYER_UNIT_ADJUST_EXPERIENCE_LEVEL"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"GDR_VETERAN_NAME",
		"Amount",
		2
	);
	
```

