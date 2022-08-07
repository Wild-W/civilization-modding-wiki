---
tags:
- EffectType
title: EFFECT_GRANT_CITY_YIELD_PERCENT_UNIT_CREATED_COST
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_GRANT_CITY_YIELD_PERCENT_UNIT_CREATED_COST
>
> * Class: `CITIES`
> * Parameters:
>	* UnitProductionPercent `Integer`
>	* YieldType `String`
>		* [Yields.YieldType]

## Samples

```SQL {title="BASILIKOI_PAIDES_SCIENCE_TRAINED_UNIT"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		RunOnce,
		Permanent
	)
VALUES
	(
		"BASILIKOI_PAIDES_SCIENCE_TRAINED_UNIT",
		"MODIFIER_SINGLE_CITY_GRANT_YIELD_PER_UNIT_COST",
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
		"BASILIKOI_PAIDES_SCIENCE_TRAINED_UNIT",
		"UnitProductionPercent",
		25
	),
	(
		"BASILIKOI_PAIDES_SCIENCE_TRAINED_UNIT",
		"YieldType",
		"YIELD_SCIENCE"
	);
	
```

