---
tags:
- EffectType
title: EFFECT_GRANT_UNIT_TYPE_UNLIMITED_PROMOTION_CHOICES
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_GRANT_UNIT_TYPE_UNLIMITED_PROMOTION_CHOICES
>
> * Class: `PLAYERS`
> * Parameters:
>	* UnitType `String`
>		* [Units.UnitType]

## Samples

```SQL {title="MINOR_CIV_YEREVAN_APOSTLE_PROMOTION_BONUS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"MINOR_CIV_YEREVAN_APOSTLE_PROMOTION_BONUS",
		"MODIFIER_PLAYER_UNIT_GRANT_UNLIMITED_PROMOTION_CHOICES"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"MINOR_CIV_YEREVAN_APOSTLE_PROMOTION_BONUS",
		"UnitType",
		"UNIT_APOSTLE"
	);
	
```

