---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_CAN_PURCHASE_DISTRICTS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_CAN_PURCHASE_DISTRICTS
>
> * Class: `CITIES`
> * Parameters:
>	* CanPurchase `Boolean`

## Samples
```SQL {title="CONTRACTOR_ENABLE_DISTRICT_PURCHASE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"CONTRACTOR_ENABLE_DISTRICT_PURCHASE",
		"MODIFIER_CITY_ADJUST_CAN_PURCHASE_DISTRICTS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"CONTRACTOR_ENABLE_DISTRICT_PURCHASE",
		"CanPurchase",
		1
	);
	
```

