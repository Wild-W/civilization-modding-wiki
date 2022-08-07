---
tags:
- EffectType
title: EFFECT_ADJUST_RELIGION_BUILDING_DISCOUNT
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_RELIGION_BUILDING_DISCOUNT
>
> * Class: `PLAYERS`
> * Parameters:
>	* Discount `Integer`

## Samples
```SQL {title="TRAIT_RELIGIOUS_BUILDING_DISCOUNT"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_RELIGIOUS_BUILDING_DISCOUNT",
		"MODIFIER_PLAYER_ADJUST_RELIGION_BUILDING_DISCOUNT"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_RELIGIOUS_BUILDING_DISCOUNT",
		"Discount",
		90
	);
	
```

