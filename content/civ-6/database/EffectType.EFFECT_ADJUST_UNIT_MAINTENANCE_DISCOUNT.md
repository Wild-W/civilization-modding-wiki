---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_MAINTENANCE_DISCOUNT
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_MAINTENANCE_DISCOUNT
>
> * Class: `UNITS`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="CONSCRIPTION_UNITMAINTENANCEDISCOUNT"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"CONSCRIPTION_UNITMAINTENANCEDISCOUNT",
		"MODIFIER_PLAYER_ADJUST_UNIT_MAINTENANCE_DISCOUNT"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"CONSCRIPTION_UNITMAINTENANCEDISCOUNT",
		"Amount",
		1
	);
	
```

