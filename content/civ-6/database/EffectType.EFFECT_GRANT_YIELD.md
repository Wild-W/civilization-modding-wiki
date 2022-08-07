---
tags:
- EffectType
title: EFFECT_GRANT_YIELD
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_GRANT_YIELD
>
> * Class: `ANY`
> * Parameters:
>	* Amount `Integer`
>	* Scale `Boolean`
>	* YieldType `String`
>		* [Yields.YieldType]

## Samples

```SQL {title="GOODY_GOLD_LARGE_MODIFIER"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		RunOnce,
		Permanent
	)
VALUES
	(
		"GOODY_GOLD_LARGE_MODIFIER",
		"MODIFIER_PLAYER_GRANT_YIELD",
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
		"GOODY_GOLD_LARGE_MODIFIER",
		"Amount",
		120
	),
	(
		"GOODY_GOLD_LARGE_MODIFIER",
		"Scale",
		1
	),
	(
		"GOODY_GOLD_LARGE_MODIFIER",
		"YieldType",
		"YIELD_GOLD"
	);
	
```

