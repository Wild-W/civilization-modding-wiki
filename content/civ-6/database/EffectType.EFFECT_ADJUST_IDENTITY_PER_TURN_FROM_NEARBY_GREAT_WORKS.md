---
tags:
- EffectType
title: EFFECT_ADJUST_IDENTITY_PER_TURN_FROM_NEARBY_GREAT_WORKS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_IDENTITY_PER_TURN_FROM_NEARBY_GREAT_WORKS
>
> * Class: `Unknown`
> * Parameters:
>	* Amount `Integer`
>	* ForeignCities `Boolean`

## Samples

```SQL {title="IDENTITY_NEARBY_GREATWORKS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"IDENTITY_NEARBY_GREATWORKS",
		"MODIFIER_PLAYER_ADJUST_IDENTITY_PER_TURN_FROM_NEARBY_GREAT_WORKS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"IDENTITY_NEARBY_GREATWORKS",
		"Amount",
		1
	),
	(
		"IDENTITY_NEARBY_GREATWORKS",
		"ForeignCities",
		1
	);
	
```

