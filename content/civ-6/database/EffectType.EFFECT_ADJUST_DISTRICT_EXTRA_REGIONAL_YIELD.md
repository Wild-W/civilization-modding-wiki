---
tags:
- EffectType
title: EFFECT_ADJUST_DISTRICT_EXTRA_REGIONAL_YIELD
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_DISTRICT_EXTRA_REGIONAL_YIELD
>
> * Class: `DISTRICTS`
> * Parameters:
>	* Amount `Integer`
>	* YieldType `String`
>		* [Yields.YieldType]

## Samples

```SQL {title="GREATPERSON_EXTRA_REGIONAL_BUILDING_PRODUCTION"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		RunOnce,
		Permanent
	)
VALUES
	(
		"GREATPERSON_EXTRA_REGIONAL_BUILDING_PRODUCTION",
		"MODIFIER_PLAYER_DISTRICT_ADJUST_EXTRA_REGIONAL_YIELD",
		1,
		1
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"GREATPERSON_EXTRA_REGIONAL_BUILDING_PRODUCTION",
		"Amount",
		2
	),
	(
		"GREATPERSON_EXTRA_REGIONAL_BUILDING_PRODUCTION",
		"YieldType",
		"YIELD_PRODUCTION"
	);
	
```

