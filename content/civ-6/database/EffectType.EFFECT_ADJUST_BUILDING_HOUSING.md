---
tags:
- EffectType
title: EFFECT_ADJUST_BUILDING_HOUSING
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_BUILDING_HOUSING
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="RELIGIOUS_COMMUNITY_SHRINE_HOUSING_MODIFIER"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"RELIGIOUS_COMMUNITY_SHRINE_HOUSING_MODIFIER",
		"MODIFIER_SINGLE_CITY_ADJUST_BUILDING_HOUSING"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"RELIGIOUS_COMMUNITY_SHRINE_HOUSING_MODIFIER",
		"Amount",
		1
	);
	
```

