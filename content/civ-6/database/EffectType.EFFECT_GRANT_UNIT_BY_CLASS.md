---
tags:
- EffectType
title: EFFECT_GRANT_UNIT_BY_CLASS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_GRANT_UNIT_BY_CLASS
>
> * Class: `CITIES`
> * Parameters:
>	* UnitPromotionClassType `String`
>		* [UnitPromotionClasses.PromotionClassType]

## Samples

```SQL {title="GOODY_MILITARY_GRANT_SCOUT"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		RunOnce,
		Permanent
	)
VALUES
	(
		"GOODY_MILITARY_GRANT_SCOUT",
		"MODIFIER_SINGLE_CITY_GRANT_UNIT_BY_CLASS_IN_NEAREST_CITY",
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
		"GOODY_MILITARY_GRANT_SCOUT",
		"UnitPromotionClassType",
		"PROMOTION_CLASS_RECON"
	);
	
```

