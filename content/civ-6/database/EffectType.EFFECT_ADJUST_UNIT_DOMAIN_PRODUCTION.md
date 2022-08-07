---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_DOMAIN_PRODUCTION
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_DOMAIN_PRODUCTION
>
> * Class: `UNITS`
> * Parameters:
>	* Amount `Integer`
>	* Domain `String`
>		* DOMAIN_AIR>		  DOMAIN_LAND>		  DOMAIN_SEA

## Samples
```SQL {title="COTHON_NAVAL_UNIT_PRODUCTION"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"COTHON_NAVAL_UNIT_PRODUCTION",
		"MODIFIER_CITY_ADJUST_UNIT_DOMAIN_PRODUCTION"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"COTHON_NAVAL_UNIT_PRODUCTION",
		"Amount",
		50
	),
	(
		"COTHON_NAVAL_UNIT_PRODUCTION",
		"Domain",
		"DOMAIN_SEA"
	);
	
```

