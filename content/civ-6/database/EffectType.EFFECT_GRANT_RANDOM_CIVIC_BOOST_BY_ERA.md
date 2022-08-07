---
tags:
- EffectType
title: EFFECT_GRANT_RANDOM_CIVIC_BOOST_BY_ERA
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_GRANT_RANDOM_CIVIC_BOOST_BY_ERA
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`
>	* EndEraType `String`
>		* [Eras.EraType]
>	* StartEraType `String`
>		* [Eras.EraType]

## Samples

```SQL {title="BUILDING_BROADWAY_RANDOMCIVICBOOST"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		RunOnce,
		Permanent
	)
VALUES
	(
		"BUILDING_BROADWAY_RANDOMCIVICBOOST",
		"MODIFIER_PLAYER_GRANT_RANDOM_CIVIC_BOOST_BY_ERA",
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
		"BUILDING_BROADWAY_RANDOMCIVICBOOST",
		"Amount",
		1
	),
	(
		"BUILDING_BROADWAY_RANDOMCIVICBOOST",
		"EndEraType",
		"ERA_ATOMIC"
	),
	(
		"BUILDING_BROADWAY_RANDOMCIVICBOOST",
		"StartEraType",
		"ERA_ATOMIC"
	);
	
```

