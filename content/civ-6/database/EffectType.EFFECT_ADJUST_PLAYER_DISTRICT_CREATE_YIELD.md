---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_DISTRICT_CREATE_YIELD
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_DISTRICT_CREATE_YIELD
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`
>	* DistrictType `String`
>		* [Districts.DistrictType]
>	* ImprovementType `String`
>		* [Improvements.ImprovementType]
>	* MustReplaceImprovement `Boolean`
>	* YieldBasedOnAppeal `Boolean`
>	* YieldType `String`
>		* [Yields.YieldType]

## Samples
```SQL {title="PUBLICTRANSPORT_FARMREPLACEGOLD"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"PUBLICTRANSPORT_FARMREPLACEGOLD",
		"MODIFIER_PLAYER_DISTRICT_CREATE_YIELD"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"PUBLICTRANSPORT_FARMREPLACEGOLD",
		"Amount",
		100
	),
	(
		"PUBLICTRANSPORT_FARMREPLACEGOLD",
		"DistrictType",
		"DISTRICT_NEIGHBORHOOD"
	),
	(
		"PUBLICTRANSPORT_FARMREPLACEGOLD",
		"ImprovementType",
		"IMPROVEMENT_FARM"
	),
	(
		"PUBLICTRANSPORT_FARMREPLACEGOLD",
		"MustReplaceImprovement",
		1
	),
	(
		"PUBLICTRANSPORT_FARMREPLACEGOLD",
		"YieldBasedOnAppeal",
		1
	),
	(
		"PUBLICTRANSPORT_FARMREPLACEGOLD",
		"YieldType",
		"YIELD_GOLD"
	);
	
```

