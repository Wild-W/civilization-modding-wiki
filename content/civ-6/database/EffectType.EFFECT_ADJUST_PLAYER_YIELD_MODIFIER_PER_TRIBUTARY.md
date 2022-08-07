---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_YIELD_MODIFIER_PER_TRIBUTARY
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_YIELD_MODIFIER_PER_TRIBUTARY
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`
>	* YieldType `String`
>		* [Yields.YieldType]

## Samples
```SQL {title="TRAIT_CULTURE_PER_CITY_STATE_TRIBUTARY"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_CULTURE_PER_CITY_STATE_TRIBUTARY",
		"MODIFIER_PLAYER_ADJUST_YIELD_MODIFIER_PER_TRIBUTARY"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_CULTURE_PER_CITY_STATE_TRIBUTARY",
		"Amount",
		5
	),
	(
		"TRAIT_CULTURE_PER_CITY_STATE_TRIBUTARY",
		"YieldType",
		"YIELD_CULTURE"
	);
	
```

