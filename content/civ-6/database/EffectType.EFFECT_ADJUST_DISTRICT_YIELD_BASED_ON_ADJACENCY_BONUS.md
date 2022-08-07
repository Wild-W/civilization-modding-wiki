---
tags:
- EffectType
title: EFFECT_ADJUST_DISTRICT_YIELD_BASED_ON_ADJACENCY_BONUS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_DISTRICT_YIELD_BASED_ON_ADJACENCY_BONUS
>
> * Class: `DISTRICTS`
> * Parameters:
>	* YieldTypeToGrant `String`
>		* [Yields.YieldType]
>	* YieldTypeToMirror `String`
>		* [Yields.YieldType]

## Samples

```SQL {title="GREATPERSON_HOLY_SITE_ADJACENCY_AS_SCIENCE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		RunOnce,
		Permanent
	)
VALUES
	(
		"GREATPERSON_HOLY_SITE_ADJACENCY_AS_SCIENCE",
		"MODIFIER_PLAYER_DISTRICT_ADJUST_YIELD_BASED_ON_ADJACENCY_BONUS",
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
		"GREATPERSON_HOLY_SITE_ADJACENCY_AS_SCIENCE",
		"YieldTypeToGrant",
		"YIELD_SCIENCE"
	),
	(
		"GREATPERSON_HOLY_SITE_ADJACENCY_AS_SCIENCE",
		"YieldTypeToMirror",
		"YIELD_FAITH"
	);
	
```

