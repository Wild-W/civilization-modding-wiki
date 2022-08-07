---
tags:
- EffectType
title: EFFECT_ADJUST_CAN_FAITH_PURCHASE_DISTRICTS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CAN_FAITH_PURCHASE_DISTRICTS
>
> * Class: `CITIES`
> * Parameters:
>	* CanPurchase `Boolean`

## Samples

```SQL {title="CARDINAL_FAITH_PURCHASE_DISTRICT"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"CARDINAL_FAITH_PURCHASE_DISTRICT",
		"MODIFIER_GOVERNOR_ADJUST_CAN_FAITH_PURCHASE_DISTRICTS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"CARDINAL_FAITH_PURCHASE_DISTRICT",
		"CanPurchase",
		1
	);
	
```

