---
tags:
- EffectType
title: EFFECT_ADJUST_DISTRICT_BUILDING_PRODUCTION
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_DISTRICT_BUILDING_PRODUCTION
>
> * Class: `DISTRICTS`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="INCREASE_DISTRICT_BUILDING_PRODUCTION"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"INCREASE_DISTRICT_BUILDING_PRODUCTION",
		"MODIFIER_ALL_CITIES_ADJUST_DISTRICT_BUILDING_PRODUCTION"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"INCREASE_DISTRICT_BUILDING_PRODUCTION",
		"Amount",
		100
	);
	
```

