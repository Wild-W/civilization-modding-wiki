---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_CORPS_ARMY_PRODUCTION
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_CORPS_ARMY_PRODUCTION
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`
>	* UnitDomain `String`
>		* DOMAIN_AIR>		  DOMAIN_LAND>		  DOMAIN_SEA

## Samples

```SQL {title="MILITARY_ACADEMY_TRAINED_CORPS_ARMY_DISCOUNT"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"MILITARY_ACADEMY_TRAINED_CORPS_ARMY_DISCOUNT",
		"MODIFIER_CITY_CORPS_ARMY_ADJUST_DISCOUNT"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"MILITARY_ACADEMY_TRAINED_CORPS_ARMY_DISCOUNT",
		"Amount",
		25
	),
	(
		"MILITARY_ACADEMY_TRAINED_CORPS_ARMY_DISCOUNT",
		"UnitDomain",
		"DOMAIN_LAND"
	);
	
```

