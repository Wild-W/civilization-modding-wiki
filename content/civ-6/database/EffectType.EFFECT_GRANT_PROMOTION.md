---
tags:
- EffectType
title: EFFECT_GRANT_PROMOTION
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_GRANT_PROMOTION
>
> * Class: `UNITS`
> * Parameters:
>	* PromotionType `String`
>		* [Promotions.PromotionType]

## Samples
```SQL {title="MONT_ST_MICHEL_GRANT_MARTYR"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		Permanent
	)
VALUES
	(
		"MONT_ST_MICHEL_GRANT_MARTYR",
		"MODIFIER_PLAYER_UNITS_GRANT_PROMOTION",
		1
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"MONT_ST_MICHEL_GRANT_MARTYR",
		"PromotionType",
		"PROMOTION_MARTYR"
	);
	
```

