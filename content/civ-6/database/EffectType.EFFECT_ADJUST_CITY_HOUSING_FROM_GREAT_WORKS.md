---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_HOUSING_FROM_GREAT_WORKS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_HOUSING_FROM_GREAT_WORKS
>
> * Class: `Unknown`
> * Parameters:
>	* Amount `Unknown`

## Samples
```SQL {title="PRODUCT_CITY_GROWTH_HOUSING_HONEY"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectStackLimit
	)
VALUES
	(
		"PRODUCT_CITY_GROWTH_HOUSING_HONEY",
		"MODIFIER_SINGLE_CITY_ADJUST_CITY_HOUSING_FROM_GREAT_WORKS",
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
		"PRODUCT_CITY_GROWTH_HOUSING_HONEY",
		"Amount",
		3
	);
	
```

