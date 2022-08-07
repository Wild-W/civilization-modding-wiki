---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_UNIT_WONDER_PERCENT
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_UNIT_WONDER_PERCENT
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="TRAIT_BUILDER_WONDER_PERCENT"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_BUILDER_WONDER_PERCENT",
		"MODIFIER_PLAYER_ADJUST_UNIT_WONDER_PERCENT"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_BUILDER_WONDER_PERCENT",
		"Amount",
		15
	);
	
```

