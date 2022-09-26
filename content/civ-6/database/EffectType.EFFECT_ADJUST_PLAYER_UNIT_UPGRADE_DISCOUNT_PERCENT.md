---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_UNIT_UPGRADE_DISCOUNT_PERCENT
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_UNIT_UPGRADE_DISCOUNT_PERCENT
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="MINOR_CIV_GOLD_MILITARY_UPGRADE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"MINOR_CIV_GOLD_MILITARY_UPGRADE",
		"MODIFIER_PLAYER_ADJUST_UNIT_UPGRADE_DISCOUNT_PERCENT"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"MINOR_CIV_GOLD_MILITARY_UPGRADE",
		"Amount",
		100
	);
	
```
