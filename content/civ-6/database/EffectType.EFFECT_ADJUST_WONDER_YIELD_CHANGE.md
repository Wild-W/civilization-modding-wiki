---
tags:
- EffectType
title: EFFECT_ADJUST_WONDER_YIELD_CHANGE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_WONDER_YIELD_CHANGE
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`
>	* YieldType `String`
>		* [Yields.YieldType]

## Samples
```SQL {title="DIVINE_INSPIRATION_WONDER_FAITH_MODIFIER"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"DIVINE_INSPIRATION_WONDER_FAITH_MODIFIER",
		"MODIFIER_SINGLE_CITY_ADJUST_WONDER_YIELD_CHANGE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"DIVINE_INSPIRATION_WONDER_FAITH_MODIFIER",
		"Amount",
		4
	),
	(
		"DIVINE_INSPIRATION_WONDER_FAITH_MODIFIER",
		"YieldType",
		"YIELD_FAITH"
	);
	
```

