---
tags:
- EffectType
title: EFFECT_GRANT_RANDOM_BASE_PROMOTION
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_GRANT_RANDOM_BASE_PROMOTION
>
> * Class: `UNITS`
> * Parameters:
>	* UnitType `String`
>		* [Promotions.PromotionType]

## Samples
```SQL {title="EMERGENCY_SOOTHSAYER_PROMOTION_TOP_TIER"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"EMERGENCY_SOOTHSAYER_PROMOTION_TOP_TIER",
		"MODIFIER_MAJOR_PLAYERS_GRANT_BASE_PROMOTION",
		"SCORED_COMPETITION_TOP_TIER_REQUIREMENTS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"EMERGENCY_SOOTHSAYER_PROMOTION_TOP_TIER",
		"UnitType",
		"UNIT_SOOTHSAYER"
	);
	
```

