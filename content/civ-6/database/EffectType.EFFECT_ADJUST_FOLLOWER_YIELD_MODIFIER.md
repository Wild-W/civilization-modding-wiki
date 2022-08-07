---
tags:
- EffectType
title: EFFECT_ADJUST_FOLLOWER_YIELD_MODIFIER
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_FOLLOWER_YIELD_MODIFIER
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`
>	* YieldType `String`
>		* [Yields.YieldType]

## Samples

```SQL {title="WORK_ETHIC_FOLLOWER_PRODUCTION_MODIFIER"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"WORK_ETHIC_FOLLOWER_PRODUCTION_MODIFIER",
		"MODIFIER_FOLLOWER_YIELD_MODIFIER"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"WORK_ETHIC_FOLLOWER_PRODUCTION_MODIFIER",
		"Amount",
		1
	),
	(
		"WORK_ETHIC_FOLLOWER_PRODUCTION_MODIFIER",
		"YieldType",
		"YIELD_PRODUCTION"
	);
	
```

