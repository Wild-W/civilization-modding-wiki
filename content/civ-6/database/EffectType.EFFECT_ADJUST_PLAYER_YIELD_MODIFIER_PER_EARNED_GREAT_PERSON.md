---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_YIELD_MODIFIER_PER_EARNED_GREAT_PERSON
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_YIELD_MODIFIER_PER_EARNED_GREAT_PERSON
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`
>	* YieldType `String`
>		* [Yields.YieldType]

## Samples

```SQL {title="MINOR_CIV_ANTANANARIVO_CULTURE_FROM_EARNED_GREAT_PEOPLE_BONUS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"MINOR_CIV_ANTANANARIVO_CULTURE_FROM_EARNED_GREAT_PEOPLE_BONUS",
		"MODIFIER_PLAYER_ADJUST_YIELD_MODIFIER_PER_EARNED_GREAT_PERSON"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"MINOR_CIV_ANTANANARIVO_CULTURE_FROM_EARNED_GREAT_PEOPLE_BONUS",
		"Amount",
		2
	),
	(
		"MINOR_CIV_ANTANANARIVO_CULTURE_FROM_EARNED_GREAT_PEOPLE_BONUS",
		"YieldType",
		"YIELD_CULTURE"
	);
	
```

