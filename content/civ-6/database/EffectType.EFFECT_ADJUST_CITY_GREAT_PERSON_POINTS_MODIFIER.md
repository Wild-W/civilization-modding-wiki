---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_GREAT_PERSON_POINTS_MODIFIER
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_GREAT_PERSON_POINTS_MODIFIER
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="EDUCATOR_INCREASE_CITY_GREAT_PERSON_POINT_BONUS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"EDUCATOR_INCREASE_CITY_GREAT_PERSON_POINT_BONUS",
		"MODIFIER_CITY_INCREASE_GREAT_PERSON_POINT_BONUS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"EDUCATOR_INCREASE_CITY_GREAT_PERSON_POINT_BONUS",
		"Amount",
		100
	);
	
```

