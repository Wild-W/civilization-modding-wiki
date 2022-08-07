---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_RELIGION_IGNORE_COMBAT
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_RELIGION_IGNORE_COMBAT
>
> * Class: `CITIES`
> * Parameters:
>	* Enable `Boolean`

## Samples

```SQL {title="CARDINAL_CITADEL_OF_GOD_COMBAT"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"CARDINAL_CITADEL_OF_GOD_COMBAT",
		"MODIFIER_SINGLE_CITY_RELIGION_IGNORE_COMBAT"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"CARDINAL_CITADEL_OF_GOD_COMBAT",
		"Enable",
		1
	);
	
```

