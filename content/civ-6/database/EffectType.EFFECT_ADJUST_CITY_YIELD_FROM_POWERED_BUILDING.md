---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_YIELD_FROM_POWERED_BUILDING
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_YIELD_FROM_POWERED_BUILDING
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`
>	* YieldType `String`

## Samples

```SQL {title="TRAIT_POWERED_BUILDINGS_MORE_CULTURE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_POWERED_BUILDINGS_MORE_CULTURE",
		"MODIFIER_PLAYER_CITIES_ADJUST_YIELD_FROM_POWERED_BUILDINGS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_POWERED_BUILDINGS_MORE_CULTURE",
		"Amount",
		4
	),
	(
		"TRAIT_POWERED_BUILDINGS_MORE_CULTURE",
		"YieldType",
		"YIELD_CULTURE"
	);
	
```

