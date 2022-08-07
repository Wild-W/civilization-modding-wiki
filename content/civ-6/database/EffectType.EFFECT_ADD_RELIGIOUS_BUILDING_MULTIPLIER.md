---
tags:
- EffectType
title: EFFECT_ADD_RELIGIOUS_BUILDING_MULTIPLIER
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADD_RELIGIOUS_BUILDING_MULTIPLIER
>
> * Class: `PLAYERS`
> * Parameters:
>	* Founder `Boolean`
>	* Multiplier `Integer`
>	* YieldType `String`
>		* [Yields.YieldType]

## Samples
```SQL {title="TRAIT_RELIGIOUS_BUILDING_MULTIPLIER_CULTURE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_RELIGIOUS_BUILDING_MULTIPLIER_CULTURE",
		"MODIFIER_PLAYER_ADD_RELIGIOUS_BUILDING_MULTIPLIER"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_RELIGIOUS_BUILDING_MULTIPLIER_CULTURE",
		"Founder",
		1
	),
	(
		"TRAIT_RELIGIOUS_BUILDING_MULTIPLIER_CULTURE",
		"Multiplier",
		10
	),
	(
		"TRAIT_RELIGIOUS_BUILDING_MULTIPLIER_CULTURE",
		"YieldType",
		"YIELD_CULTURE"
	);
	
```

