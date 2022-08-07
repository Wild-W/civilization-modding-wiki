---
tags:
- EffectType
title: EFFECT_ADJUST_ALL_BUILDING_PRODUCTION_MODIFIER
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_ALL_BUILDING_PRODUCTION_MODIFIER
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`
>	* IsWonder `Boolean`

## Samples

```SQL {title="KILWA_SINGLE_ADDPRODUCTIONBUILDINGS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"KILWA_SINGLE_ADDPRODUCTIONBUILDINGS",
		"MODIFIER_SINGLE_CITY_ADJUST_BUILDING_PRODUCTION_MODIFIER",
		"INDUSTRIAL_SUZERAIN_1_REQUIREMENTS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"KILWA_SINGLE_ADDPRODUCTIONBUILDINGS",
		"Amount",
		15
	);
	
```


```SQL {title="TRAIT_LESS_BUILDING_PRODUCTION"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_LESS_BUILDING_PRODUCTION",
		"MODIFIER_PLAYER_CITIES_ADJUST_BUILDING_PRODUCTION_MODIFIER"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_LESS_BUILDING_PRODUCTION",
		"Amount",
		"-30"
	),
	(
		"TRAIT_LESS_BUILDING_PRODUCTION",
		"IsWonder",
		0
	);
	
```

