---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_ALLOWED_INCOMING_REGIONAL_STACKING
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_ALLOWED_INCOMING_REGIONAL_STACKING
>
> * Class: `CITIES`
> * Parameters:
>	* YieldType `String`
>		* [Yields.YieldType]

## Samples

```SQL {title="VERTICAL_INTEGRATION_PRODUCTION_REGIONAL_STACKING"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"VERTICAL_INTEGRATION_PRODUCTION_REGIONAL_STACKING",
		"MODIFIER_CITY_ADJUST_ALLOWED_INCOMING_REGIONAL_STACKING"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"VERTICAL_INTEGRATION_PRODUCTION_REGIONAL_STACKING",
		"YieldType",
		"YIELD_PRODUCTION"
	);
	
```

