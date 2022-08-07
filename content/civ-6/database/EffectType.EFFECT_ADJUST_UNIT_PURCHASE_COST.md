---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_PURCHASE_COST
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_PURCHASE_COST
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`
>	* UnitType `String`
>		* [Units.UnitType]

## Samples
```SQL {title="HOLY_ORDER_MISSIONARY_DISCOUNT_MODIFIER"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"HOLY_ORDER_MISSIONARY_DISCOUNT_MODIFIER",
		"MODIFIER_PLAYER_CITIES_ADJUST_UNIT_PURCHASE_COST"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"HOLY_ORDER_MISSIONARY_DISCOUNT_MODIFIER",
		"Amount",
		30
	),
	(
		"HOLY_ORDER_MISSIONARY_DISCOUNT_MODIFIER",
		"UnitType",
		"UNIT_MISSIONARY"
	);
	
```

