---
tags:
- EffectType
title: EFFECT_GRANT_UNIT_OF_CLASS_AND_APPLY_ABILITY
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_GRANT_UNIT_OF_CLASS_AND_APPLY_ABILITY
>
> * Class: `CITIES`
> * Parameters:
>	* ModifierId `String`
>		* [Units.UnitType]
>	* UnitPromotionClassType `String`
>		* [Units.UnitType]

## Samples
```SQL {title="GOODY_METEOR_FREE_UNIT"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		RunOnce,
		Permanent
	)
VALUES
	(
		"GOODY_METEOR_FREE_UNIT",
		"MODIFIER_PLAYER_GRANT_ADVANCED_UNIT_OF_CLASS_IN_NEAREST_OWNER_CITY_AND_APPLY_ABILITY",
		1,
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
		"GOODY_METEOR_FREE_UNIT",
		"ModifierId",
		"GOODY_METEOR_UNIT_REFUND_COST"
	),
	(
		"GOODY_METEOR_FREE_UNIT",
		"UnitPromotionClassType",
		"PROMOTION_CLASS_HEAVY_CAVALRY"
	);
	
```

