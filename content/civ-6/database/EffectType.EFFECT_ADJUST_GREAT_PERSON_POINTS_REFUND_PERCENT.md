---
tags:
- EffectType
title: EFFECT_ADJUST_GREAT_PERSON_POINTS_REFUND_PERCENT
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_GREAT_PERSON_POINTS_REFUND_PERCENT
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="TRAIT_GREAT_PERSON_REFUND"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_GREAT_PERSON_REFUND",
		"MODIFIER_PLAYER_ADJUST_GREAT_PERSON_POINTS_REFUND_PERCENT"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_GREAT_PERSON_REFUND",
		"Amount",
		20
	);
	
```

