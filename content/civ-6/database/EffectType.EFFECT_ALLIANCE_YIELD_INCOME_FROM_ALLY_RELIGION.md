---
tags:
- EffectType
title: EFFECT_ALLIANCE_YIELD_INCOME_FROM_ALLY_RELIGION
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ALLIANCE_YIELD_INCOME_FROM_ALLY_RELIGION
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`
>	* YieldType `String`
>		* [Yields.YieldType]

## Samples
```SQL {title="ALLIANCE_YIELDS_FROM_FOLLOWING_ALLY_RELIGION"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"ALLIANCE_YIELDS_FROM_FOLLOWING_ALLY_RELIGION",
		"MODIFIER_ALLIANCE_PLAYERS_YIELD_FROM_FOLLOWERS_OF_ALLY_RELIGIONS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"ALLIANCE_YIELDS_FROM_FOLLOWING_ALLY_RELIGION",
		"Amount",
		1
	),
	(
		"ALLIANCE_YIELDS_FROM_FOLLOWING_ALLY_RELIGION",
		"YieldType",
		"YIELD_FAITH"
	);
	
```

