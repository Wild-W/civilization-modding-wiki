---
tags:
- EffectType
title: EFFECT_ADJUST_DISTRICT_YIELD_MODIFIER
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_DISTRICT_YIELD_MODIFIER
>
> * Class: `DISTRICTS`
> * Parameters:
>	* Amount `Integer`
>	* YieldType `String`
>		* [Yields.YieldType]

## Samples

```SQL {title="AESTHETICS_DISTRICTCULTURE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"AESTHETICS_DISTRICTCULTURE",
		"MODIFIER_PLAYER_DISTRICTS_ADJUST_YIELD_MODIFIER",
		"DISTRICT_IS_THEATER"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"AESTHETICS_DISTRICTCULTURE",
		"Amount",
		100
	),
	(
		"AESTHETICS_DISTRICTCULTURE",
		"YieldType",
		"YIELD_CULTURE"
	);
	
```

