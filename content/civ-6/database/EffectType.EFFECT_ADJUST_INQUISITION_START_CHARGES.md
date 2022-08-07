---
tags:
- EffectType
title: EFFECT_ADJUST_INQUISITION_START_CHARGES
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_INQUISITION_START_CHARGES
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="INQUISITION_REDUCE_START_CHARGES"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"INQUISITION_REDUCE_START_CHARGES",
		"MODIFIER_PLAYER_ADJUST_INQUISITION_START_CHARGES"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"INQUISITION_REDUCE_START_CHARGES",
		"Amount",
		1
	);
	
```

