---
tags:
- EffectType
title: EFFECT_ADJUST_RESOURCE_YIELD_BY_COUNT
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_RESOURCE_YIELD_BY_COUNT
>
> * Class: `GOVERNORS`
> * Parameters:
>	* Amount `Integer`
>	* YieldType `String`

## Samples

```SQL {title="TRAIT_FAITH_RESOURCES"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_FAITH_RESOURCES",
		"MODIFIER_PLAYER_CITIES_ADJUST_RESOURCE_YIELD_BY_COUNT"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_FAITH_RESOURCES",
		"Amount",
		1
	),
	(
		"TRAIT_FAITH_RESOURCES",
		"YieldType",
		"YIELD_FAITH"
	);
	
```

