---
tags:
- EffectType
title: EFFECT_ADJUST_YIELD_BY_NUMBER_OF_RESOURCES
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_YIELD_BY_NUMBER_OF_RESOURCES
>
> * Class: `Unknown`
> * Parameters:
>	* Amount `Unknown`
>	* YieldType `Unknown`

## Samples

```SQL {title="MINOR_CIV_JOHANNESBURG_PRODUCTION_RESOURCES"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"MINOR_CIV_JOHANNESBURG_PRODUCTION_RESOURCES",
		"MODIFIER_PLAYER_CITIES_ADJUST_YIELD_BY_NUMBER_RESOURCES"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"MINOR_CIV_JOHANNESBURG_PRODUCTION_RESOURCES",
		"Amount",
		1
	),
	(
		"MINOR_CIV_JOHANNESBURG_PRODUCTION_RESOURCES",
		"YieldType",
		"YIELD_PRODUCTION"
	);
	
```

