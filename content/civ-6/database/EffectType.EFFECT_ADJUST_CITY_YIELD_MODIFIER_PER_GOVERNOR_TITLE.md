---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_YIELD_MODIFIER_PER_GOVERNOR_TITLE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_YIELD_MODIFIER_PER_GOVERNOR_TITLE
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`
>	* YieldType `String`
>		* [Yields.YieldType]

## Samples
```SQL {title="TRAIT_ADJUST_CITY_CULTURE_PER_GOVERNOR_TITLE_MODIFIER"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_ADJUST_CITY_CULTURE_PER_GOVERNOR_TITLE_MODIFIER",
		"MODIFIER_PLAYER_CITIES_ADJUST_CITY_YIELD_MODIFIER_PER_GOVERNOR_TITLE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_ADJUST_CITY_CULTURE_PER_GOVERNOR_TITLE_MODIFIER",
		"Amount",
		3
	),
	(
		"TRAIT_ADJUST_CITY_CULTURE_PER_GOVERNOR_TITLE_MODIFIER",
		"YieldType",
		"YIELD_CULTURE"
	);
	
```

