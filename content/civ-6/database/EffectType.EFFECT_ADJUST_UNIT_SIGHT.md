---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_SIGHT
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_SIGHT
>
> * Class: `UNITS`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="SPYGLASS_BONUS_SIGHT"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"SPYGLASS_BONUS_SIGHT",
		"MODIFIER_PLAYER_UNIT_ADJUST_SIGHT"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"SPYGLASS_BONUS_SIGHT",
		"Amount",
		1
	);
	
```

