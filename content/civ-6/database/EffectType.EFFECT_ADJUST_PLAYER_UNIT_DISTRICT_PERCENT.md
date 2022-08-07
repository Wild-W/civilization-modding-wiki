---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_UNIT_DISTRICT_PERCENT
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_UNIT_DISTRICT_PERCENT
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="TRAIT_BUILDER_DISTRICT_PERCENT"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_BUILDER_DISTRICT_PERCENT",
		"MODIFIER_PLAYER_ADJUST_UNIT_DISTRICT_PERCENT"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_BUILDER_DISTRICT_PERCENT",
		"Amount",
		20
	);
	
```

