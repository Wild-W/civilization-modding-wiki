---
tags:
- EffectType
title: EFFECT_ADJUST_ALL_DISTRICTS_PURCHASE_COST
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_ALL_DISTRICTS_PURCHASE_COST
>
> * Class: `Unknown`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="SUGUBA_CHEAPER_DISTRICT_PURCHASE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"SUGUBA_CHEAPER_DISTRICT_PURCHASE",
		"MODIFIER_SINGLE_CITY_ADJUST_ALL_DISTRICTS_PURCHASE_COST"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"SUGUBA_CHEAPER_DISTRICT_PURCHASE",
		"Amount",
		20
	);
	
```

